# BashBot - Interactive Bash Command Helper 🤖

BashBot is an interactive CLI tool that provides instant explanations, syntax help, and practical examples for common bash and development commands. Never forget command syntax again!

## Features ✨

- **📚 Comprehensive Command Database**: Pre-loaded with 172+ commands across 10 categories:
  - **Development**: `git`, `npm`, `pip`, `docker`, `pytest`
  - **Python**: `venv` (create, activate, deactivate, install, freeze, troubleshoot)
  - **Localhost**: `localhost` (kill dev servers, find ports, manage local projects)
  - **Windows**: `powershell` (Get-Process, Stop-Process, etc.), `cmd` (netstat, tasklist, etc.)
  - **Linux/Ubuntu**: `linux` (ls, grep, ps, kill, chmod, apt, etc.)

- **🎨 Beautiful Terminal Output**: Color-coded, easy-to-read command information
- **🔍 Smart Search**: Find commands by name or description
- **💡 Practical Examples**: Real-world usage examples for every command
- **⚡ Interactive Mode**: REPL-style interface for quick lookups
- **📖 Detailed Documentation**: Syntax, flags, and explanations for each command
- **🖥️ Cross-Platform**: Works on Windows (PowerShell, CMD), Linux, and macOS
- **📋 List All Flags Mode**: Condensed view of ALL available flags/options for quick reference
- **📄 Cheat Sheet Generator**: Create comprehensive single-page reference cards
- **🚀 Global Access**: Quick `bb` command available from anywhere in PowerShell

## Installation 

### Basic Installation (Local Testing)

1. Clone or navigate to the project directory:
```bash
cd c:\Users\William\OneDrive\Desktop\AppIdeas\bashCommands
```

2. No dependencies required! Uses Python standard library only.

### Make it Globally Available (Optional)

To use `bashbot` from anywhere:

1. Create a `setup.py` file (see below)
2. Install in development mode:
```bash
pip install -e .
```

3. Now run `bashbot` from anywhere!

## Usage 

### Interactive Mode

Start BashBot in interactive mode:

```bash
python bashbot.py
```

Then type commands to get help:
```
bashbot> git
bashbot> git commit
bashbot> search push
bashbot> list
bashbot> exit
```

### Command-Line Mode

Get help directly from the command line:

```bash
# Show all commands
python bashbot.py list

# Show git subcommands
python bashbot.py git

# Show git commit details
python bashbot.py git commit

# Search for commands
python bashbot.py search clone
```

### Usage Examples

#### Example 1: Learn about git commit
```bash
$ python bashbot.py git commit
```
Output shows:
- Description of what `git commit` does
- Syntax: `git commit [options]`
- Common flags (`-m`, `-a`, `--amend`, etc.)
- Practical examples with explanations

#### Example 2: Find all push-related commands
```bash
$ python bashbot.py search push
```

#### Example 3: Interactive exploration
```bash
$ python bashbot.py -i
bashbot> docker
# Shows all docker subcommands
bashbot> docker run
# Shows detailed help for docker run
```

## Command Line Options

```bash
python bashbot.py [options] [command]

Options:
  -i, --interactive    Start in interactive mode
  -l, --list-all       Show condensed list of ALL flags/options
  -c, --cheatsheet     Generate comprehensive cheat sheet
  --no-color          Disable colored output
  -h, --help          Show help message

Arguments:
  command             Command to look up (e.g., "git commit")

Examples:
  python bashbot.py git                # Show git subcommands
  python bashbot.py git commit         # Show git commit details
  python bashbot.py -l cmd taskkill    # Show ALL taskkill flags (condensed)
  python bashbot.py -c git             # Generate git cheat sheet
```

## Global Access (Recommended)

Run the setup script to use `bb` from anywhere:

```powershell
cd c:\Users\William\OneDrive\Desktop\AppIdeas\bashCommands
.\setup_bashbot.ps1
```

Then restart PowerShell or run: `. $PROFILE`

Now you can use:
```powershell
bb git commit              # Quick lookup
bbflags taskkill           # Show all flags
bbcheat git                # Generate cheat sheet
```

## Project Structure 

```
bashCommands/
├── bashbot.py              # Main CLI application
├── commands/               # Command database (JSON files)
│   ├── git.json           # Git version control
│   ├── npm.json           # Node.js package manager
│   ├── pip.json           # Python package manager
│   ├── docker.json        # Docker containers
│   ├── pytest.json        # Python testing
│   ├── venv.json          # Python virtual environments
│   ├── localhost.json     # Localhost/port management
│   ├── powershell.json    # Windows PowerShell
│   ├── cmd.json           # Windows Command Prompt
│   └── linux.json         # Linux/Ubuntu commands
├── core/                   # Core modules
│   ├── __init__.py
│   ├── database.py         # Database loader
│   ├── formatter.py        # Terminal output formatting
│   └── search.py           # Search functionality
├── requirements.txt
└── README.md
```

## Available Commands

Currently includes comprehensive help for:

**Development Tools:**
- **git**: 21 subcommands (clone, commit, push, pull, branch, merge, rebase, etc.)
- **npm**: 15 subcommands (install, run, test, publish, etc.)
- **pip**: 13 subcommands (install, list, freeze, etc.)
- **docker**: 18 subcommands (run, build, ps, exec, compose, etc.)
- **pytest**: 10 common testing patterns and flags

**Python Virtual Environments:**
- **venv**: 17 subcommands for managing Python virtual environments
  - Create and activate venv (PowerShell, CMD, Linux)
  - Run scripts without activating venv
  - Install, list, and freeze packages
  - Troubleshoot common venv issues
  - Clone venv to another machine
  - Check which venv is active

**Localhost/Port Management:**
- **localhost**: 15 commands for managing dev servers and ports
  - Find what's running on any port (PowerShell, CMD, Linux)
  - Kill processes on specific ports
  - Kill all dev servers at once
  - List all localhost connections
  - Quick reference for common dev ports

**Windows Commands:**
- **powershell**: 22 PowerShell commands (Get-Process, Stop-Process, Get-Service, Get-ChildItem, etc.)
- **cmd**: 20 Command Prompt commands (netstat, tasklist, taskkill, ipconfig, findstr, etc.)

**Linux/Ubuntu Commands:**
- **linux**: 30+ bash commands (ls, grep, find, ps, kill, chmod, tar, curl, systemctl, apt, etc.)

## Adding New Commands 🔧

To add a new command:

1. Create a JSON file in the `commands/` directory (e.g., `commands/yarn.json`)
2. Follow this structure:

```json
{
  "commandname": {
    "description": "Brief description",
    "subcommands": {
      "subcommand1": {
        "syntax": "commandname subcommand1 [options]",
        "description": "What this subcommand does",
        "flags": [
          {
            "flag": "-f, --flag",
            "description": "What this flag does"
          }
        ],
        "examples": [
          {
            "command": "commandname subcommand1 --flag",
            "explanation": "What this example demonstrates"
          }
        ]
      }
    }
  }
}
```

3. Restart BashBot - it will automatically load the new command!

## Making BashBot Globally Available 

### Option 1: Create setup.py

Create a `setup.py` file in the project root:

```python
from setuptools import setup, find_packages

setup(
    name='bashbot',
    version='1.0.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[],
    entry_points={
        'console_scripts': [
            'bashbot=bashbot:main',
        ],
    },
    package_data={
        '': ['commands/*.json'],
    },
)
```

Then install:
```bash
pip install -e .
```

### Option 2: Add to PATH (Windows)

1. Create a batch file `bashbot.bat`:
```batch
@echo off
python "C:\Users\William\OneDrive\Desktop\AppIdeas\bashCommands\bashbot.py" %*
```

2. Add the directory to your PATH or copy to a directory already in PATH

### Option 3: Create alias (Linux/Mac)

Add to your `~/.bashrc` or `~/.zshrc`:
```bash
alias bashbot='python /path/to/bashCommands/bashbot.py'
```

## Future Enhancements 

Potential improvements:
- [ ] Add more commands (curl, wget, ssh, rsync, etc.)
- [ ] System commands (ls, grep, find, chmod, etc.)
- [ ] Autocomplete in interactive mode
- [ ] Export command cheat sheets to PDF/Markdown
- [ ] Integration with `man` pages
- [ ] Custom user commands/aliases
- [ ] Command history in interactive mode
- [ ] Fuzzy matching for typos
- [ ] Context-aware suggestions

## Contributing 

To add more commands or improve existing ones:

1. Edit the appropriate JSON file in `commands/`
2. Follow the existing format
3. Include clear, practical examples
4. Test with `python bashbot.py <your-command>`

## License 

Free to use and modify for personal and commercial projects.

## Support 

If you find this helpful, consider:
- Adding more commands to the database
- Sharing with other developers
- Providing feedback on which commands to add next

---

**Made with  for developers who can never remember all those flags and options!**
