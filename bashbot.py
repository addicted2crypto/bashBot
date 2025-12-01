#!/usr/bin/env python3
"""
BashBot - Interactive bash command helper
Provides explanations, syntax, and examples for common bash/CLI commands
"""

import sys
import argparse
from pathlib import Path

# Add the current directory to the path to import core modules
sys.path.insert(0, str(Path(__file__).parent))

from core import (CommandDatabase, CommandFormatter, CommandSearch, CommandHistory,
                  copy_to_clipboard, is_clipboard_available, ContextDetector)


class BashBot:
    """Main BashBot CLI application"""

    def __init__(self, copy_mode: bool = False):
        """
        Initialize BashBot with database, formatter, search, and history

        Args:
            copy_mode: If True, copy command syntax to clipboard after display
        """
        try:
            self.db = CommandDatabase()
            self.formatter = CommandFormatter(use_colors=True)
            self.search = CommandSearch(self.db)
            self.history = CommandHistory()
            self.copy_mode = copy_mode
        except Exception as e:
            print(f"Error initializing BashBot: {e}")
            sys.exit(1)

    # Helper methods for cleaner code organization
    def _lookup_command(self, command_name: str) -> tuple:
        """
        Look up a command and return (command_data, error_message)

        Args:
            command_name: Name of command to look up

        Returns:
            Tuple of (command_data, error_message). If successful, error_message is None.
        """
        command_data = self.db.get_command(command_name)

        if not command_data:
            error_msg = self.formatter.format_error(f"Command '{command_name}' not found")
            suggestions = self.search.suggest_command(command_name)
            if suggestions:
                error_msg += f"\n\nDid you mean: {', '.join(suggestions[:3])}?"
            return None, error_msg

        return command_data, None

    def _lookup_subcommand(self, command_name: str, subcommand_name: str) -> tuple:
        """
        Look up a subcommand and return (subcommand_data, error_message)

        Args:
            command_name: Name of parent command
            subcommand_name: Name of subcommand

        Returns:
            Tuple of (subcommand_data, error_message). If successful, error_message is None.
        """
        subcommand_data = self.db.get_subcommand(command_name, subcommand_name)

        if not subcommand_data:
            error_msg = self.formatter.format_error(
                f"Subcommand '{command_name} {subcommand_name}' not found")
            suggestions = self.search.suggest_subcommand(command_name, subcommand_name)
            if suggestions:
                error_msg += f"\n\nDid you mean: {', '.join(suggestions[:3])}?"
            return None, error_msg

        return subcommand_data, None

    def _parse_query(self, query: str) -> tuple:
        """
        Parse a query string into command and subcommand parts

        Args:
            query: Query string (e.g., 'git commit')

        Returns:
            Tuple of (command_name, subcommand_name). subcommand_name may be None.
        """
        parts = query.split()

        if len(parts) == 0:
            return None, None

        command_name = parts[0].lower()
        subcommand_name = parts[1].lower() if len(parts) > 1 else None

        return command_name, subcommand_name

    def _copy_syntax_to_clipboard(self, subcommand_data: dict):
        """
        Copy command syntax to clipboard if copy_mode is enabled

        Args:
            subcommand_data: Subcommand data dictionary containing syntax
        """
        if not self.copy_mode:
            return

        if not is_clipboard_available():
            print("\n[Clipboard not available on this system]")
            return

        syntax = subcommand_data.get('syntax', '')
        if syntax:
            if copy_to_clipboard(syntax):
                print(f"\n[Copied to clipboard: {syntax}]")
            else:
                print("\n[Failed to copy to clipboard]")

    def run_interactive(self):
        """Run in interactive mode"""
        print(self.formatter.format_welcome())

        while True:
            try:
                user_input = input(self.formatter._color("\nbashbot> ",
                                   self.formatter._color("", "")))
                user_input = user_input.strip()

                if not user_input:
                    continue

                # Handle exit commands
                if user_input.lower() in ['exit', 'quit', 'q']:
                    print(self.formatter._color("\nGoodbye!",
                          self.formatter._color("", "")))
                    break

                # Handle special commands
                if user_input.lower() == 'list':
                    self._handle_list()
                elif user_input.lower().startswith('search '):
                    query = user_input[7:].strip()
                    self._handle_search(query)
                elif user_input.lower().startswith('flags '):
                    query = user_input[6:].strip()
                    self._handle_flags(query)
                elif user_input.lower().startswith('quick '):
                    query = user_input[6:].strip()
                    self._handle_quick(query)
                elif user_input.lower() == 'history':
                    self._handle_history()
                elif user_input.lower() == 'stats':
                    self._handle_history(show_stats=True)
                elif user_input.lower() == 'smart':
                    self._handle_smart()
                elif user_input.lower() == 'help':
                    print(self.formatter.format_welcome())
                else:
                    # Handle regular command queries
                    self._handle_query(user_input)

            except KeyboardInterrupt:
                print(self.formatter._color("\n\nGoodbye!",
                      self.formatter._color("", "")))
                break
            except EOFError:
                print(self.formatter._color("\n\nGoodbye!",
                      self.formatter._color("", "")))
                break
            except Exception as e:
                print(self.formatter.format_error(f"Unexpected error: {e}"))

    def run_command(self, args: list, list_all: bool = False, cheatsheet: bool = False,
                    show_history: bool = False, show_stats: bool = False, smart: bool = False):
        """
        Run in command mode with arguments

        Args:
            args: List of command arguments
            list_all: Show condensed list of all flags
            cheatsheet: Generate cheat sheet for command
            show_history: Show recent command history
            show_stats: Show most used commands
            smart: Show smart context-aware suggestions
        """
        # Handle special modes first (they don't need args)
        if smart:
            self._handle_smart()
            return

        if show_history or show_stats:
            self._handle_history(show_stats=show_stats)
            return

        if not args:
            self._handle_list()
            return

        # Check for search command
        if args[0].lower() == 'search':
            query = ' '.join(args[1:])
            self._handle_search(query)
            return

        # Check for list command
        if args[0].lower() == 'list':
            self._handle_list()
            return

        # Handle regular command query
        query = ' '.join(args)

        if cheatsheet:
            self._handle_cheatsheet(query)
        elif list_all:
            self._handle_flags(query)
        else:
            self._handle_query(query)

    def _handle_list(self):
        """Handle the 'list' command"""
        commands = self.db.list_commands()
        print(self.formatter.format_command_list(commands))

    def _handle_search(self, query: str):
        """Handle search queries"""
        if not query:
            print(self.formatter.format_error("Please provide a search query"))
            return

        cmd_matches, subcmd_matches = self.search.search(query)
        print(self.formatter.format_search_results(query, cmd_matches, subcmd_matches))

    def _handle_query(self, query: str):
        """
        Handle a command query

        Args:
            query: User query (e.g., 'git', 'git commit')
        """
        command_name, subcommand_name = self._parse_query(query)

        if not command_name:
            return

        # Look up command
        command_data, error = self._lookup_command(command_name)
        if error:
            print(error)
            return

        # If only command name provided, show subcommands
        if not subcommand_name:
            subcommands = self.db.list_subcommands(command_name)
            description = command_data.get('description', '')
            print(self.formatter.format_subcommand_list(
                command_name, subcommands, description))
            return

        # Look up subcommand
        subcommand_data, error = self._lookup_subcommand(command_name, subcommand_name)
        if error:
            print(error)
            return

        # Track command in history
        self.history.add_command(command_name, subcommand_name)

        # Display subcommand details
        print(self.formatter.format_subcommand_details(
            command_name, subcommand_name, subcommand_data))

        # Copy syntax to clipboard if copy mode is enabled
        self._copy_syntax_to_clipboard(subcommand_data)

    def _handle_flags(self, query: str):
        """
        Handle flags/list-all mode - shows condensed list of all flags for a command

        Args:
            query: Command query (e.g., 'taskkill', 'git commit')
        """
        command_name, subcommand_name = self._parse_query(query)

        if not command_name:
            print(self.formatter.format_error("Please specify a command"))
            return

        # Look up command
        command_data, error = self._lookup_command(command_name)
        if error:
            print(error)
            return

        # If subcommand specified, show flags for that subcommand
        if subcommand_name:
            subcommand_data, error = self._lookup_subcommand(command_name, subcommand_name)
            if error:
                print(error)
                return

            print(self.formatter.format_flags_list(command_name, subcommand_name, subcommand_data))
        else:
            # Show all flags from all subcommands
            subcommands = command_data.get('subcommands', {})
            print(self.formatter.format_all_flags(command_name, subcommands))

    def _handle_quick(self, query: str):
        """
        Handle quick reference mode - condensed command reference

        Args:
            query: Command query
        """
        command_name, _ = self._parse_query(query)

        if not command_name:
            print(self.formatter.format_error("Please specify a command"))
            return

        # Look up command
        command_data, error = self._lookup_command(command_name)
        if error:
            print(error)
            return

        subcommands = command_data.get('subcommands', {})
        print(self.formatter.format_quick_reference(command_name, subcommands))

    def _handle_cheatsheet(self, query: str):
        """
        Handle cheatsheet mode - comprehensive single-page reference

        Args:
            query: Command query
        """
        command_name, _ = self._parse_query(query)

        if not command_name:
            print(self.formatter.format_error("Please specify a command"))
            return

        # Look up command
        command_data, error = self._lookup_command(command_name)
        if error:
            print(error)
            return

        subcommands = command_data.get('subcommands', {})
        description = command_data.get('description', '')
        print(self.formatter.format_cheatsheet(command_name, subcommands, description))

    def _handle_history(self, show_stats: bool = False):
        """
        Handle history display - shows recent or most used commands

        Args:
            show_stats: If True, show most used commands. Otherwise show recent.
        """
        if show_stats:
            # Show most frequently used commands
            most_used = self.history.get_most_used(limit=10)
            if not most_used:
                print("No command history yet.")
                return

            print("\n" + "=" * 50)
            print("MOST USED COMMANDS")
            print("=" * 50)
            for item in most_used:
                print(f"  {item['count']:>3}x  {item['query']}")
            print("")
        else:
            # Show recent commands
            recent = self.history.get_recent(limit=10)
            if not recent:
                print("No command history yet.")
                return

            print("\n" + "=" * 50)
            print("RECENT COMMANDS")
            print("=" * 50)
            for entry in recent:
                timestamp = entry['timestamp'][:19].replace('T', ' ')  # Format timestamp
                print(f"  {timestamp}  {entry['full_query']}")
            print("")

    def _handle_smart(self):
        """
        Handle smart context detection - suggests commands based on current directory
        """
        detector = ContextDetector()
        report = detector.format_context_report()
        print(report)


def main():
    """Main entry point"""
    parser = argparse.ArgumentParser(
        description='BashBot - Interactive bash command helper',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  bashbot                    # Start interactive mode
  bashbot list               # List all available commands
  bashbot git                # Show git subcommands
  bashbot git commit         # Show git commit details
  bashbot search push        # Search for commands containing 'push'
  bashbot -l taskkill        # Show all taskkill flags (condensed)
  bashbot -c git             # Generate git cheat sheet
  bashbot --history          # Show recent command history
  bashbot --stats            # Show most used commands
  bashbot --copy git commit  # Show details and copy syntax to clipboard
  bashbot --smart            # Detect project type and suggest commands

Interactive mode commands:
  list                       # Show all commands
  search <query>             # Search commands
  flags <command>            # Show all flags for command (condensed)
  quick <command>            # Quick reference for command
  history                    # Show recent command history
  stats                      # Show most used commands
  smart                      # Detect project context and suggest commands
  <command>                  # Show subcommands (e.g., 'git')
  <command> <subcommand>     # Show details (e.g., 'git commit')
  exit, quit, q              # Exit interactive mode
        """
    )

    parser.add_argument(
        'args',
        nargs='*',
        help='Command to look up (e.g., "git commit") or "list" to show all commands'
    )

    parser.add_argument(
        '-i', '--interactive',
        action='store_true',
        help='Start in interactive mode'
    )

    parser.add_argument(
        '--no-color',
        action='store_true',
        help='Disable colored output'
    )

    parser.add_argument(
        '-l', '--list-all',
        action='store_true',
        help='Show condensed list of all flags/options for a command'
    )

    parser.add_argument(
        '-c', '--cheatsheet',
        action='store_true',
        help='Generate comprehensive cheat sheet for a command'
    )

    parser.add_argument(
        '--history',
        action='store_true',
        help='Show recent command history'
    )

    parser.add_argument(
        '--stats',
        action='store_true',
        help='Show most frequently used commands'
    )

    parser.add_argument(
        '--copy',
        action='store_true',
        help='Copy command syntax to clipboard after display'
    )

    parser.add_argument(
        '--smart',
        action='store_true',
        help='Detect project context and suggest relevant commands'
    )

    parsed_args = parser.parse_args()

    # Create BashBot instance
    bot = BashBot(copy_mode=parsed_args.copy)

    # Disable colors if requested
    if parsed_args.no_color:
        bot.formatter.use_colors = False

    # Run in appropriate mode
    # Check for special flags that don't require args first
    if parsed_args.smart or parsed_args.history or parsed_args.stats:
        bot.run_command(parsed_args.args,
                       list_all=parsed_args.list_all,
                       cheatsheet=parsed_args.cheatsheet,
                       show_history=parsed_args.history,
                       show_stats=parsed_args.stats,
                       smart=parsed_args.smart)
    elif parsed_args.interactive or not parsed_args.args:
        bot.run_interactive()
    else:
        bot.run_command(parsed_args.args,
                       list_all=parsed_args.list_all,
                       cheatsheet=parsed_args.cheatsheet,
                       show_history=parsed_args.history,
                       show_stats=parsed_args.stats,
                       smart=parsed_args.smart)


if __name__ == '__main__':
    main()
