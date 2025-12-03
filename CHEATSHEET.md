# BashBot Command Cheatsheet

Quick reference for all available commands in BashBot. Use `bashbot <command> <subcommand>` for detailed help.

Last Updated: 2025-11-30
Total Commands: 14 | Total Subcommands: 200+

---

## Version Control

### **git** (21 subcommands)
Essential Git version control commands
```bash
bashbot git status      # Check repository status
bashbot git commit      # Commit changes
bashbot git push        # Push to remote
bashbot git pull        # Pull from remote
bashbot git branch      # Manage branches
bashbot git merge       # Merge branches
bashbot git rebase      # Rebase branches
bashbot git log         # View commit history
bashbot git diff        # Show changes
bashbot git clone       # Clone repository
```

---

## Package Managers

### **npm** (15 subcommands)
Node.js package manager
```bash
bashbot npm install     # Install dependencies
bashbot npm run         # Run package scripts
bashbot npm test        # Run tests
bashbot npm start       # Start dev server
bashbot npm publish     # Publish package
```

### **yarn** (13 subcommands) ✨ NEW
Fast JavaScript package manager with caching
```bash
bashbot yarn install    # Install all dependencies
bashbot yarn add        # Add new package
bashbot yarn remove     # Remove package
bashbot yarn upgrade    # Update packages
bashbot yarn run        # Run script
bashbot yarn workspaces # Manage monorepo
```

### **pip** (13 subcommands)
Python package installer
```bash
bashbot pip install     # Install packages
bashbot pip list        # List installed
bashbot pip freeze      # Export requirements
bashbot pip uninstall   # Remove packages
```

---

## Containers & Virtualization

### **docker** (18 subcommands)
Container management
```bash
bashbot docker run      # Run container
bashbot docker build    # Build image
bashbot docker ps       # List containers
bashbot docker exec     # Execute in container
bashbot docker compose  # Multi-container apps
bashbot docker logs     # View container logs
```

### **venv** (17 subcommands)
Python virtual environments
```bash
bashbot venv create     # Create new venv
bashbot venv activate   # Activate venv
bashbot venv deactivate # Deactivate venv
bashbot venv install    # Install in venv
```

---

## Testing

### **pytest** (10 subcommands)
Python testing framework
```bash
bashbot pytest          # Run tests
bashbot pytest verbose  # Verbose output
bashbot pytest coverage # Test coverage
bashbot pytest watch    # Watch mode
```

---

## Network & Remote Access

### **curl** (10 subcommands) ✨ NEW
HTTP requests and API testing
```bash
bashbot curl get        # GET request
bashbot curl post       # POST request
bashbot curl put        # PUT request
bashbot curl delete     # DELETE request
bashbot curl auth       # Authentication
bashbot curl headers    # Custom headers
bashbot curl download   # Download files
```

### **ssh** (10 subcommands) ✨ NEW
Secure Shell remote access
```bash
bashbot ssh connect     # Connect to server
bashbot ssh keygen      # Generate SSH keys
bashbot ssh copy-id     # Copy key to server
bashbot ssh tunnel      # Port forwarding
bashbot ssh scp         # Secure file copy
bashbot ssh agent       # Key management
bashbot ssh config      # Client configuration
```

### **localhost** (15 subcommands)
Local development server management
```bash
bashbot localhost kill  # Kill process on port
bashbot localhost find  # Find what's on port
bashbot localhost list  # List all connections
```

---

## Text Processing & Search

### **grep** (10 subcommands) ✨ NEW
Pattern searching in files
```bash
bashbot grep search     # Basic search
bashbot grep regex      # Regular expressions
bashbot grep context    # Show surrounding lines
bashbot grep files      # File operations
bashbot grep count      # Count matches
bashbot grep invert     # Exclude patterns
```

---

## System Commands

### **powershell** (22 subcommands)
Windows PowerShell commands
```bash
bashbot powershell Get-Process
bashbot powershell Stop-Process
bashbot powershell Get-Service
bashbot powershell Get-ChildItem
```

### **cmd** (20 subcommands)
Windows Command Prompt
```bash
bashbot cmd netstat     # Network statistics
bashbot cmd tasklist    # List processes
bashbot cmd taskkill    # Kill process
bashbot cmd ipconfig    # Network config
```

### **linux** (30+ subcommands)
Linux/Unix commands
```bash
bashbot linux ls        # List files
bashbot linux grep      # Search text
bashbot linux find      # Find files
bashbot linux ps        # Process status
bashbot linux chmod     # Change permissions
bashbot linux tar       # Archive files
bashbot linux curl      # Transfer data
bashbot linux systemctl # Service management
```

---

## BashBot Features

### Command History
```bash
bashbot --history       # Show recent commands
bashbot --stats         # Most used commands
```

### Context Detection
```bash
bashbot --smart         # Auto-detect project type
```

### Clipboard Integration
```bash
bashbot --copy git commit  # Copy syntax to clipboard
```

### Quick Reference Modes
```bash
bashbot -l git             # List all flags
bashbot -c git             # Generate cheat sheet
bashbot search clone       # Search commands
```

---

## Command Categories Summary

| Category | Commands | Subcommands |
|----------|----------|-------------|
| Version Control | git | 21 |
| Package Managers | npm, yarn, pip | 41 |
| Containers | docker, venv | 35 |
| Testing | pytest | 10 |
| Network | curl, ssh, localhost | 35 |
| Text Processing | grep | 10 |
| System (Windows) | powershell, cmd | 42 |
| System (Linux) | linux | 30+ |
| **TOTAL** | **14 commands** | **224+** |

---

## Recently Added Commands ✨

- **curl** (2025-11-30) - HTTP requests and API testing
- **yarn** (2025-11-30) - JavaScript package manager
- **ssh** (2025-11-30) - Secure remote access
- **grep** (2025-11-30) - Text pattern searching

---

## Usage Tips

### Interactive Mode
```bash
python bashbot.py
bashbot> git commit     # Interactive exploration
bashbot> history        # View command history
bashbot> smart          # Context-aware suggestions
bashbot> exit
```

### Command Line Mode
```bash
python bashbot.py git commit          # Direct lookup
python bashbot.py --copy curl post    # Copy syntax
python bashbot.py --smart             # Smart suggestions
```

### Search & Discovery
```bash
python bashbot.py search "port"       # Find commands about ports
python bashbot.py list                # List all commands
python bashbot.py flags docker        # Show all docker flags
```

---

## Contributing New Commands

To add a new command, create a JSON file in `commands/` directory:

```json
{
  "commandname": {
    "description": "Brief description",
    "subcommands": {
      "subcommand1": {
        "syntax": "command syntax",
        "description": "What it does",
        "flags": [...],
        "examples": [...]
      }
    }
  }
}
```

BashBot automatically loads all JSON files from the `commands/` directory!

---

## Quick Links

- [Full Documentation](README.md)
- [Quick Start Guide](QUICK_START.md)
- [Commands Directory](commands/)
- [Report Issues](https://github.com/YOUR_USERNAME/bashbot/issues)

---

**Built with ❤️ for developers who forget command syntax**

*Stay tuned for more command additions: kubectl, make, terraform, and more!*
