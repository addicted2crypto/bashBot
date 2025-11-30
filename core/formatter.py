"""
Formatter module for displaying command information in terminal
"""

from typing import Dict, List, Optional


class Colors:
    """ANSI color codes for terminal output"""
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'
    GRAY = '\033[90m'


class CommandFormatter:
    """Formats command data for terminal display"""

    def __init__(self, use_colors: bool = True):
        """
        Initialize the formatter

        Args:
            use_colors: Whether to use ANSI color codes
        """
        self.use_colors = use_colors

    def _color(self, text: str, color: str) -> str:
        """Apply color to text if colors are enabled"""
        if self.use_colors:
            return f"{color}{text}{Colors.END}"
        return text

    def format_command_list(self, commands: List[str]) -> str:
        """
        Format a list of available commands

        Args:
            commands: List of command names

        Returns:
            Formatted string
        """
        output = []
        output.append(self._color("Available Commands:", Colors.BOLD + Colors.CYAN))
        output.append("")

        for cmd in commands:
            output.append(f"  {self._color('*', Colors.GREEN)} {self._color(cmd, Colors.YELLOW)}")

        output.append("")
        output.append(self._color("Tip:", Colors.GRAY) +
                     " Use 'bashbot <command>' to see subcommands (e.g., 'bashbot git')")

        return "\n".join(output)

    def format_subcommand_list(self, command_name: str, subcommands: List[str],
                               description: str = "") -> str:
        """
        Format a list of subcommands for a command

        Args:
            command_name: Name of the main command
            subcommands: List of subcommand names
            description: Command description

        Returns:
            Formatted string
        """
        output = []
        output.append(self._color(f"{command_name.upper()}", Colors.BOLD + Colors.CYAN))

        if description:
            output.append(self._color(description, Colors.GRAY))

        output.append("")
        output.append(self._color("Subcommands:", Colors.BOLD))
        output.append("")

        for subcmd in subcommands:
            output.append(f"  {self._color('*', Colors.GREEN)} {self._color(subcmd, Colors.YELLOW)}")

        output.append("")
        example_subcmd = subcommands[0] if subcommands else "..."
        output.append(self._color("Tip:", Colors.GRAY) +
                     f" Use 'bashbot {command_name} <subcommand>' for details " +
                     f"(e.g., 'bashbot {command_name} {example_subcmd}')")

        return "\n".join(output)

    def format_subcommand_details(self, command_name: str, subcommand_name: str,
                                   data: Dict) -> str:
        """
        Format detailed information about a subcommand

        Args:
            command_name: Name of the main command
            subcommand_name: Name of the subcommand
            data: Subcommand data dictionary

        Returns:
            Formatted string
        """
        output = []

        # Header
        full_command = f"{command_name} {subcommand_name}"
        output.append(self._color("=" * 70, Colors.CYAN))
        output.append(self._color(f"  {full_command.upper()}", Colors.BOLD + Colors.CYAN))
        output.append(self._color("=" * 70, Colors.CYAN))
        output.append("")

        # Description
        if 'description' in data:
            output.append(self._color("Description:", Colors.BOLD + Colors.YELLOW))
            output.append(f"  {data['description']}")
            output.append("")

        # Syntax
        if 'syntax' in data:
            output.append(self._color("Syntax:", Colors.BOLD + Colors.YELLOW))
            output.append(f"  {self._color(data['syntax'], Colors.GREEN)}")
            output.append("")

        # Flags/Options
        if 'flags' in data and data['flags']:
            output.append(self._color("Common Flags:", Colors.BOLD + Colors.YELLOW))
            for flag in data['flags']:
                flag_text = self._color(f"  {flag['flag']}", Colors.CYAN)
                desc_text = flag['description']
                output.append(f"{flag_text}")
                output.append(f"    {desc_text}")
            output.append("")

        # Examples
        if 'examples' in data and data['examples']:
            output.append(self._color("Examples:", Colors.BOLD + Colors.YELLOW))
            for i, example in enumerate(data['examples'], 1):
                output.append(f"  {self._color(f'{i}.', Colors.GRAY)} {example['explanation']}")
                output.append(f"     {self._color('$', Colors.GREEN)} {self._color(example['command'], Colors.BOLD)}")
                if i < len(data['examples']):
                    output.append("")

        output.append("")
        output.append(self._color("-" * 70, Colors.GRAY))

        return "\n".join(output)

    def format_error(self, message: str) -> str:
        """
        Format an error message

        Args:
            message: Error message

        Returns:
            Formatted error string
        """
        return self._color(f"X Error: {message}", Colors.RED)

    def format_search_results(self, query: str, command_matches: List[str],
                              subcommand_matches: Dict[str, List[str]]) -> str:
        """
        Format search results

        Args:
            query: Search query
            command_matches: List of matching command names
            subcommand_matches: Dict of command -> list of matching subcommands

        Returns:
            Formatted search results
        """
        output = []
        output.append(self._color(f"Search results for: '{query}'", Colors.BOLD + Colors.CYAN))
        output.append("")

        if command_matches:
            output.append(self._color("Commands:", Colors.BOLD + Colors.YELLOW))
            for cmd in command_matches:
                output.append(f"  {self._color('*', Colors.GREEN)} {self._color(cmd, Colors.YELLOW)}")
            output.append("")

        if subcommand_matches:
            output.append(self._color("Subcommands:", Colors.BOLD + Colors.YELLOW))
            for cmd, subcmds in subcommand_matches.items():
                for subcmd in subcmds:
                    full = f"{cmd} {subcmd}"
                    output.append(f"  {self._color('*', Colors.GREEN)} {self._color(full, Colors.YELLOW)}")
            output.append("")

        if not command_matches and not subcommand_matches:
            output.append(self._color(f"No results found for '{query}'", Colors.GRAY))

        return "\n".join(output)

    def format_welcome(self) -> str:
        """
        Format welcome message for interactive mode

        Returns:
            Formatted welcome message
        """
        output = []
        output.append(self._color("=" * 46, Colors.CYAN))
        output.append(self._color("     BashBot - Command Helper", Colors.BOLD + Colors.CYAN))
        output.append(self._color("=" * 46, Colors.CYAN))
        output.append("")
        output.append("Type a command to get help:")
        output.append(f"  * {self._color('git', Colors.YELLOW)} - Show git subcommands")
        output.append(f"  * {self._color('git commit', Colors.YELLOW)} - Show git commit details")
        output.append(f"  * {self._color('flags git', Colors.YELLOW)} - Show all git flags (condensed)")
        output.append(f"  * {self._color('quick git', Colors.YELLOW)} - Quick reference for git")
        output.append(f"  * {self._color('list', Colors.YELLOW)} - Show all available commands")
        output.append(f"  * {self._color('search <query>', Colors.YELLOW)} - Search commands")
        output.append(f"  * {self._color('exit', Colors.YELLOW)} or {self._color('quit', Colors.YELLOW)} - Exit")
        output.append("")

        return "\n".join(output)

    def format_flags_list(self, command_name: str, subcommand_name: str, data: Dict) -> str:
        """
        Format condensed list of flags for a specific subcommand

        Args:
            command_name: Name of the main command
            subcommand_name: Name of the subcommand
            data: Subcommand data dictionary

        Returns:
            Formatted flags list
        """
        output = []
        full_command = f"{command_name} {subcommand_name}"
        output.append(self._color(f"{full_command.upper()} - FLAGS", Colors.BOLD + Colors.CYAN))
        output.append("")

        if 'syntax' in data:
            output.append(f"{self._color('Syntax:', Colors.YELLOW)} {data['syntax']}")
            output.append("")

        if 'flags' in data and data['flags']:
            # Calculate max flag length for alignment
            max_flag_len = max((len(flag['flag']) for flag in data['flags']), default=0)

            for flag in data['flags']:
                flag_text = self._color(flag['flag'].ljust(max_flag_len + 2), Colors.CYAN)
                desc_text = flag['description']
                output.append(f"  {flag_text} {desc_text}")
        else:
            output.append(self._color("  No flags available for this command", Colors.GRAY))

        output.append("")
        return "\n".join(output)

    def format_all_flags(self, command_name: str, subcommands: Dict) -> str:
        """
        Format condensed list of ALL flags from all subcommands

        Args:
            command_name: Name of the main command
            subcommands: Dictionary of subcommand data

        Returns:
            Formatted all flags list
        """
        output = []
        output.append(self._color(f"{command_name.upper()} - ALL FLAGS", Colors.BOLD + Colors.CYAN))
        output.append("")

        for subcmd_name, subcmd_data in subcommands.items():
            if 'flags' in subcmd_data and subcmd_data['flags']:
                output.append(self._color(f"{subcmd_name}:", Colors.YELLOW))

                # Calculate max flag length for alignment
                max_flag_len = max((len(flag['flag']) for flag in subcmd_data['flags']), default=0)

                for flag in subcmd_data['flags']:
                    flag_text = self._color(flag['flag'].ljust(max_flag_len + 2), Colors.CYAN)
                    desc_text = flag['description']
                    output.append(f"  {flag_text} {desc_text}")

                output.append("")

        if len(output) == 2:  # Only header present
            output.append(self._color("No flags found for this command", Colors.GRAY))

        return "\n".join(output)

    def format_quick_reference(self, command_name: str, subcommands: Dict) -> str:
        """
        Format quick reference - condensed overview of all subcommands

        Args:
            command_name: Name of the main command
            subcommands: Dictionary of subcommand data

        Returns:
            Formatted quick reference
        """
        output = []
        output.append(self._color(f"{command_name.upper()} - QUICK REFERENCE", Colors.BOLD + Colors.CYAN))
        output.append("")

        # Calculate max subcmd length for alignment
        max_subcmd_len = max((len(name) for name in subcommands.keys()), default=0)

        for subcmd_name, subcmd_data in subcommands.items():
            subcmd_text = self._color(subcmd_name.ljust(max_subcmd_len + 2), Colors.YELLOW)
            desc_text = subcmd_data.get('description', 'No description')

            # Truncate description if too long
            if len(desc_text) > 60:
                desc_text = desc_text[:57] + "..."

            output.append(f"  {subcmd_text} {self._color(desc_text, Colors.GRAY)}")

        output.append("")
        output.append(self._color(f"Tip: Use 'bashbot {command_name} <subcommand>' for details", Colors.GRAY))
        output.append("")

        return "\n".join(output)

    def format_cheatsheet(self, command_name: str, subcommands: Dict, description: str = "") -> str:
        """
        Format comprehensive cheat sheet for a command

        Args:
            command_name: Name of the main command
            subcommands: Dictionary of subcommand data
            description: Command description

        Returns:
            Formatted cheat sheet
        """
        output = []
        output.append(self._color("=" * 70, Colors.CYAN))
        output.append(self._color(f"  {command_name.upper()} CHEAT SHEET", Colors.BOLD + Colors.CYAN))
        output.append(self._color("=" * 70, Colors.CYAN))
        output.append("")

        if description:
            output.append(self._color(description, Colors.GRAY))
            output.append("")

        for subcmd_name, subcmd_data in subcommands.items():
            # Subcommand header
            output.append(self._color(f"{subcmd_name}", Colors.BOLD + Colors.YELLOW))

            # Description
            if 'description' in subcmd_data:
                output.append(f"  {subcmd_data['description']}")

            # Syntax
            if 'syntax' in subcmd_data:
                output.append(f"  {self._color('$', Colors.GREEN)} {self._color(subcmd_data['syntax'], Colors.BOLD)}")

            # Flags (condensed)
            if 'flags' in subcmd_data and subcmd_data['flags']:
                flags_str = ", ".join([flag['flag'] for flag in subcmd_data['flags']])
                if len(flags_str) > 60:
                    flags_str = flags_str[:57] + "..."
                output.append(f"  {self._color('Flags:', Colors.CYAN)} {flags_str}")

            # First example only (for space)
            if 'examples' in subcmd_data and subcmd_data['examples']:
                example = subcmd_data['examples'][0]
                output.append(f"  {self._color('Example:', Colors.CYAN)} {example['command']}")

            output.append("")

        output.append(self._color("=" * 70, Colors.GRAY))

        return "\n".join(output)
