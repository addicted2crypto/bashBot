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

from core import CommandDatabase, CommandFormatter, CommandSearch


class BashBot:
    """Main BashBot CLI application"""

    def __init__(self):
        """Initialize BashBot with database, formatter, and search"""
        try:
            self.db = CommandDatabase()
            self.formatter = CommandFormatter(use_colors=True)
            self.search = CommandSearch(self.db)
        except Exception as e:
            print(f"Error initializing BashBot: {e}")
            sys.exit(1)

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

    def run_command(self, args: list, list_all: bool = False, cheatsheet: bool = False):
        """
        Run in command mode with arguments

        Args:
            args: List of command arguments
            list_all: Show condensed list of all flags
            cheatsheet: Generate cheat sheet for command
        """
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
        parts = query.split()

        if len(parts) == 0:
            return

        command_name = parts[0].lower()

        # Check if command exists
        command_data = self.db.get_command(command_name)

        if not command_data:
            print(self.formatter.format_error(
                f"Command '{command_name}' not found"))

            # Suggest similar commands
            suggestions = self.search.suggest_command(command_name)
            if suggestions:
                print(f"\nDid you mean: {', '.join(suggestions[:3])}?")
            return

        # If only command name provided, show subcommands
        if len(parts) == 1:
            subcommands = self.db.list_subcommands(command_name)
            description = command_data.get('description', '')
            print(self.formatter.format_subcommand_list(
                command_name, subcommands, description))
            return

        # If subcommand provided, show details
        subcommand_name = parts[1].lower()
        subcommand_data = self.db.get_subcommand(command_name, subcommand_name)

        if not subcommand_data:
            print(self.formatter.format_error(
                f"Subcommand '{command_name} {subcommand_name}' not found"))

            # Suggest similar subcommands
            suggestions = self.search.suggest_subcommand(command_name, subcommand_name)
            if suggestions:
                print(f"\nDid you mean: {', '.join(suggestions[:3])}?")
            return

        # Display subcommand details
        print(self.formatter.format_subcommand_details(
            command_name, subcommand_name, subcommand_data))

    def _handle_flags(self, query: str):
        """
        Handle flags/list-all mode - shows condensed list of all flags for a command

        Args:
            query: Command query (e.g., 'taskkill', 'git commit')
        """
        parts = query.split()

        if len(parts) == 0:
            print(self.formatter.format_error("Please specify a command"))
            return

        command_name = parts[0].lower()
        command_data = self.db.get_command(command_name)

        if not command_data:
            print(self.formatter.format_error(f"Command '{command_name}' not found"))
            return

        # If subcommand specified, show flags for that subcommand
        if len(parts) > 1:
            subcommand_name = parts[1].lower()
            subcommand_data = self.db.get_subcommand(command_name, subcommand_name)

            if not subcommand_data:
                print(self.formatter.format_error(
                    f"Subcommand '{command_name} {subcommand_name}' not found"))
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
        parts = query.split()

        if len(parts) == 0:
            print(self.formatter.format_error("Please specify a command"))
            return

        command_name = parts[0].lower()
        command_data = self.db.get_command(command_name)

        if not command_data:
            print(self.formatter.format_error(f"Command '{command_name}' not found"))
            return

        subcommands = command_data.get('subcommands', {})
        print(self.formatter.format_quick_reference(command_name, subcommands))

    def _handle_cheatsheet(self, query: str):
        """
        Handle cheatsheet mode - comprehensive single-page reference

        Args:
            query: Command query
        """
        parts = query.split()

        if len(parts) == 0:
            print(self.formatter.format_error("Please specify a command"))
            return

        command_name = parts[0].lower()
        command_data = self.db.get_command(command_name)

        if not command_data:
            print(self.formatter.format_error(f"Command '{command_name}' not found"))
            return

        subcommands = command_data.get('subcommands', {})
        description = command_data.get('description', '')
        print(self.formatter.format_cheatsheet(command_name, subcommands, description))


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

Interactive mode commands:
  list                       # Show all commands
  search <query>             # Search commands
  flags <command>            # Show all flags for command (condensed)
  quick <command>            # Quick reference for command
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

    parsed_args = parser.parse_args()

    # Create BashBot instance
    bot = BashBot()

    # Disable colors if requested
    if parsed_args.no_color:
        bot.formatter.use_colors = False

    # Run in appropriate mode
    if parsed_args.interactive or not parsed_args.args:
        bot.run_interactive()
    else:
        bot.run_command(parsed_args.args,
                       list_all=parsed_args.list_all,
                       cheatsheet=parsed_args.cheatsheet)


if __name__ == '__main__':
    main()
