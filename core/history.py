"""
Command history tracking module for BashBot
Stores and retrieves command usage history
"""

import json
from pathlib import Path
from datetime import datetime
from typing import List, Dict, Optional


class CommandHistory:
    """Manages command history tracking"""

    def __init__(self, history_file: Optional[Path] = None):
        """
        Initialize command history

        Args:
            history_file: Path to history file. Defaults to ~/.bashbot/history.json
        """
        if history_file is None:
            # Default to ~/.bashbot/history.json
            home = Path.home()
            bashbot_dir = home / '.bashbot'
            bashbot_dir.mkdir(exist_ok=True)
            history_file = bashbot_dir / 'history.json'

        self.history_file = history_file
        self._ensure_history_file()

    def _ensure_history_file(self):
        """Ensure history file exists"""
        if not self.history_file.exists():
            self.history_file.write_text('[]')

    def add_command(self, command: str, subcommand: Optional[str] = None):
        """
        Add a command to history

        Args:
            command: Command name (e.g., 'git')
            subcommand: Optional subcommand name (e.g., 'commit')
        """
        history = self._load_history()

        entry = {
            'timestamp': datetime.now().isoformat(),
            'command': command,
            'subcommand': subcommand,
            'full_query': f"{command} {subcommand}" if subcommand else command
        }

        history.append(entry)

        # Keep only last 100 entries
        if len(history) > 100:
            history = history[-100:]

        self._save_history(history)

    def get_recent(self, limit: int = 10) -> List[Dict]:
        """
        Get recent command history

        Args:
            limit: Maximum number of entries to return

        Returns:
            List of recent history entries
        """
        history = self._load_history()
        return history[-limit:][::-1]  # Reverse to show most recent first

    def get_most_used(self, limit: int = 10) -> List[Dict]:
        """
        Get most frequently used commands

        Args:
            limit: Maximum number of entries to return

        Returns:
            List of (query, count) tuples sorted by frequency
        """
        history = self._load_history()

        # Count occurrences
        counts = {}
        for entry in history:
            query = entry['full_query']
            counts[query] = counts.get(query, 0) + 1

        # Sort by count
        sorted_counts = sorted(counts.items(), key=lambda x: x[1], reverse=True)

        # Return top N
        return [{'query': q, 'count': c} for q, c in sorted_counts[:limit]]

    def clear(self):
        """Clear all history"""
        self._save_history([])

    def _load_history(self) -> List[Dict]:
        """Load history from file"""
        try:
            with open(self.history_file, 'r') as f:
                return json.load(f)
        except (json.JSONDecodeError, FileNotFoundError):
            return []

    def _save_history(self, history: List[Dict]):
        """Save history to file"""
        with open(self.history_file, 'w') as f:
            json.dump(history, f, indent=2)
