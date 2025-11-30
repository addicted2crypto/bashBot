"""
Search module for finding commands and subcommands
"""

from typing import Dict, List, Tuple
from .database import CommandDatabase


class CommandSearch:
    """Handles searching through commands and subcommands"""

    def __init__(self, database: CommandDatabase):
        """
        Initialize the search module

        Args:
            database: CommandDatabase instance
        """
        self.db = database

    def search(self, query: str) -> Tuple[List[str], Dict[str, List[str]]]:
        """
        Search for commands and subcommands matching the query

        Args:
            query: Search string

        Returns:
            Tuple of (command_matches, subcommand_matches)
            - command_matches: List of matching command names
            - subcommand_matches: Dict mapping command -> list of matching subcommands
        """
        query_lower = query.lower()
        command_matches = []
        subcommand_matches = {}

        # Search in command names
        for cmd_name in self.db.list_commands():
            if query_lower in cmd_name.lower():
                command_matches.append(cmd_name)

            # Search in subcommands for this command
            subcmd_list = self.db.list_subcommands(cmd_name)
            matching_subcmds = [
                subcmd for subcmd in subcmd_list
                if query_lower in subcmd.lower()
            ]

            if matching_subcmds:
                subcommand_matches[cmd_name] = matching_subcmds

        # Also search in descriptions
        desc_matches = self._search_descriptions(query_lower)

        # Merge results
        for cmd in desc_matches:
            if cmd not in command_matches:
                command_matches.append(cmd)

        return sorted(command_matches), subcommand_matches

    def _search_descriptions(self, query: str) -> List[str]:
        """
        Search for query in command and subcommand descriptions

        Args:
            query: Search string (lowercase)

        Returns:
            List of command names with matching descriptions
        """
        matches = []

        for cmd_name in self.db.list_commands():
            command_data = self.db.get_command(cmd_name)
            if not command_data:
                continue

            # Check main command description
            main_desc = command_data.get('description', '').lower()
            if query in main_desc:
                if cmd_name not in matches:
                    matches.append(cmd_name)

            # Check subcommand descriptions
            subcommands = command_data.get('subcommands', {})
            for subcmd_name, subcmd_data in subcommands.items():
                subcmd_desc = subcmd_data.get('description', '').lower()
                if query in subcmd_desc:
                    if cmd_name not in matches:
                        matches.append(cmd_name)
                    break

        return matches

    def fuzzy_find(self, query: str, threshold: float = 0.6) -> List[Tuple[str, float]]:
        """
        Fuzzy search for commands (finds similar matches)

        Args:
            query: Search string
            threshold: Minimum similarity score (0.0 to 1.0)

        Returns:
            List of tuples (command_name, similarity_score) sorted by score
        """
        query_lower = query.lower()
        results = []

        for cmd_name in self.db.list_commands():
            score = self._similarity_score(query_lower, cmd_name.lower())
            if score >= threshold:
                results.append((cmd_name, score))

            # Also check subcommands
            for subcmd_name in self.db.list_subcommands(cmd_name):
                full_name = f"{cmd_name} {subcmd_name}"
                score = self._similarity_score(query_lower, subcmd_name.lower())
                if score >= threshold:
                    results.append((full_name, score))

        # Sort by score (descending)
        results.sort(key=lambda x: x[1], reverse=True)
        return results

    def _similarity_score(self, s1: str, s2: str) -> float:
        """
        Calculate simple similarity score between two strings

        Args:
            s1: First string
            s2: Second string

        Returns:
            Similarity score between 0.0 and 1.0
        """
        # Simple substring matching score
        if s1 == s2:
            return 1.0

        if s1 in s2 or s2 in s1:
            return 0.8

        # Count matching characters in order
        matches = 0
        s1_idx = 0

        for char in s1:
            try:
                s1_idx = s2.index(char, s1_idx) + 1
                matches += 1
            except ValueError:
                continue

        return matches / max(len(s1), len(s2))

    def suggest_command(self, partial: str) -> List[str]:
        """
        Suggest commands based on partial input

        Args:
            partial: Partial command string

        Returns:
            List of suggested command completions
        """
        partial_lower = partial.lower()
        suggestions = []

        # First, try direct prefix matches
        for cmd_name in self.db.list_commands():
            if cmd_name.lower().startswith(partial_lower):
                suggestions.append(cmd_name)

        # If no prefix matches, try contains
        if not suggestions:
            for cmd_name in self.db.list_commands():
                if partial_lower in cmd_name.lower():
                    suggestions.append(cmd_name)

        return sorted(suggestions)

    def suggest_subcommand(self, command: str, partial: str) -> List[str]:
        """
        Suggest subcommands based on partial input

        Args:
            command: Main command name
            partial: Partial subcommand string

        Returns:
            List of suggested subcommand completions
        """
        partial_lower = partial.lower()
        suggestions = []

        subcommands = self.db.list_subcommands(command)

        # Try prefix matches first
        for subcmd in subcommands:
            if subcmd.lower().startswith(partial_lower):
                suggestions.append(subcmd)

        # If no prefix matches, try contains
        if not suggestions:
            for subcmd in subcommands:
                if partial_lower in subcmd.lower():
                    suggestions.append(subcmd)

        return sorted(suggestions)
