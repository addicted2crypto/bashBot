"""
Database module for loading and managing command data
"""

import json
import os
from pathlib import Path
from typing import Dict, Optional, List


class CommandDatabase:
    """Handles loading and accessing command data from JSON files"""

    def __init__(self, commands_dir: Optional[str] = None):
        """
        Initialize the command database

        Args:
            commands_dir: Path to directory containing command JSON files.
                         If None, uses default 'commands' directory.
        """
        if commands_dir is None:
            # Get the directory where this file is located
            current_file = Path(__file__)
            project_root = current_file.parent.parent
            commands_dir = project_root / "commands"

        self.commands_dir = Path(commands_dir)
        self.commands: Dict[str, Dict] = {}
        self._load_all_commands()

    def _load_all_commands(self):
        """Load all command JSON files from the commands directory"""
        if not self.commands_dir.exists():
            raise FileNotFoundError(f"Commands directory not found: {self.commands_dir}")

        json_files = list(self.commands_dir.glob("*.json"))

        if not json_files:
            raise ValueError(f"No JSON command files found in: {self.commands_dir}")

        for json_file in json_files:
            try:
                with open(json_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    # Merge the loaded data into commands dict
                    self.commands.update(data)
            except json.JSONDecodeError as e:
                print(f"Error loading {json_file}: {e}")
            except Exception as e:
                print(f"Unexpected error loading {json_file}: {e}")

    def get_command(self, command_name: str) -> Optional[Dict]:
        """
        Get command data by name

        Args:
            command_name: Name of the command (e.g., 'git', 'npm')

        Returns:
            Command data dictionary or None if not found
        """
        return self.commands.get(command_name.lower())

    def get_subcommand(self, command_name: str, subcommand_name: str) -> Optional[Dict]:
        """
        Get subcommand data

        Args:
            command_name: Name of the main command (e.g., 'git')
            subcommand_name: Name of the subcommand (e.g., 'commit')

        Returns:
            Subcommand data dictionary or None if not found
        """
        command = self.get_command(command_name)
        if not command:
            return None

        subcommands = command.get('subcommands', {})

        # Case-insensitive lookup
        subcommand_lower = subcommand_name.lower()
        for key, value in subcommands.items():
            if key.lower() == subcommand_lower:
                return value

        return None

    def list_commands(self) -> List[str]:
        """
        Get list of all available commands

        Returns:
            List of command names
        """
        return sorted(self.commands.keys())

    def list_subcommands(self, command_name: str) -> List[str]:
        """
        Get list of all subcommands for a command

        Args:
            command_name: Name of the command

        Returns:
            List of subcommand names or empty list if command not found
        """
        command = self.get_command(command_name)
        if not command:
            return []

        subcommands = command.get('subcommands', {})
        return sorted(subcommands.keys())

    def search_commands(self, query: str) -> List[str]:
        """
        Search for commands matching a query string

        Args:
            query: Search string

        Returns:
            List of matching command names
        """
        query_lower = query.lower()
        matches = []

        for cmd_name in self.commands.keys():
            if query_lower in cmd_name.lower():
                matches.append(cmd_name)

        return sorted(matches)

    def search_subcommands(self, command_name: str, query: str) -> List[str]:
        """
        Search for subcommands matching a query string

        Args:
            command_name: Name of the command
            query: Search string

        Returns:
            List of matching subcommand names
        """
        command = self.get_command(command_name)
        if not command:
            return []

        query_lower = query.lower()
        matches = []

        subcommands = command.get('subcommands', {})
        for subcmd_name in subcommands.keys():
            if query_lower in subcmd_name.lower():
                matches.append(subcmd_name)

        return sorted(matches)
