# BashBot Quick Start Guide

## Installation (5 seconds)

### Make BashBot globally available:
```powershell
cd c:\Users\William\OneDrive\Desktop\AppIdeas\bashCommands
.\setup_bashbot.ps1
```

Then restart PowerShell or run: `. $PROFILE`

## Usage

### Quick Commands (from anywhere):
```powershell
bb git commit              # Show git commit details
bbflags taskkill           # Show ALL taskkill flags (condensed)
bbcheat git                # Generate full git cheat sheet
```

### New List Modes:
```powershell
# From command line:
python bashbot.py -l cmd taskkill     # All flags for taskkill
python bashbot.py -c git              # Git cheat sheet

# Interactive mode:
python bashbot.py
bashbot> flags powershell             # All PowerShell flags
bashbot> quick git                    # Quick git reference
```

### What's New?

**List All Flags Mode** (`-l` or `flags`)
- Shows ALL available flags/options in condensed format
- Perfect for quickly seeing what's available
- Forces learning by presenting choices upfront

**Cheat Sheet Mode** (`-c` or `bbcheat`)
- Comprehensive single-page reference
- All subcommands with syntax and examples
- Great for printing or keeping open while working

**Quick Reference** (`quick`)
- Condensed overview of all subcommands
- One-liner descriptions
- Fastest way to see what's available

## Examples

### Learn taskkill flags:
```powershell
bbflags cmd taskkill
```
Output:
```
CMD TASKKILL - FLAGS

Syntax: taskkill [/PID <pid> | /IM <imagename>] [options]

  /PID <pid>        Kill process by PID
  /IM <imagename>   Kill process by image name
  /F                Force terminate process
  /T                Kill process and all child processes
```

### Git cheat sheet:
```powershell
bbcheat git
```
Shows complete git reference with syntax, flags, and examples for all 21 git commands.

### See all PowerShell flags:
```powershell
bbflags powershell
```
Shows ALL flags from ALL PowerShell commands in aligned, easy-to-scan format.

## Tips

- Use `bb` for quick lookups
- Use `bbflags` when you need to see all options
- Use `bbcheat` to generate printable reference cards
- Interactive mode (`python bashbot.py`) for exploring

## Global Functions Added:

- `bb` - Quick lookup
- `bbflags` - Show all flags (uses `-l`)
- `bbcheat` - Generate cheat sheet (uses `-c`)

All commands support the same syntax as `python bashbot.py`
