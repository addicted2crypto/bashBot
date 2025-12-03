# BashBot Master Command Reference

**Complete reference for all 224+ commands** | Last Updated: 2025-11-30

Quick access: Use `bashbot <command> <subcommand>` for full details with examples.

---

## Table of Contents

- [Version Control](#version-control) (git)
- [Package Managers](#package-managers) (npm, yarn, pip)
- [Containers & Virtual Environments](#containers--virtual-environments) (docker, venv)
- [Testing](#testing) (pytest)
- [Network & Remote](#network--remote) (curl, ssh, localhost)
- [Text Processing](#text-processing) (grep)
- [Windows System](#windows-system) (powershell, cmd)
- [Linux System](#linux-system) (linux)
- [BashBot Features](#bashbot-features)

---

## Version Control

### git (21 subcommands)

| Subcommand | Syntax | Description |
|------------|--------|-------------|
| `clone` | `git clone <repository> [directory]` | Clone a repository |
| `init` | `git init [directory]` | Initialize new repository |
| `status` | `git status [options]` | Show working tree status |
| `add` | `git add <pathspec>` | Add files to staging |
| `commit` | `git commit [options]` | Record changes |
| `push` | `git push [remote] [branch]` | Push to remote |
| `pull` | `git pull [remote] [branch]` | Fetch and merge |
| `fetch` | `git fetch [remote]` | Download objects |
| `branch` | `git branch [options]` | List/create/delete branches |
| `checkout` | `git checkout <branch>` | Switch branches |
| `merge` | `git merge <branch>` | Merge branches |
| `rebase` | `git rebase <branch>` | Reapply commits |
| `log` | `git log [options]` | Show commit history |
| `diff` | `git diff [options]` | Show changes |
| `reset` | `git reset [options] [commit]` | Reset current HEAD |
| `stash` | `git stash [options]` | Stash changes |
| `tag` | `git tag [options]` | Create/list tags |
| `remote` | `git remote [options]` | Manage remotes |
| `config` | `git config [options]` | Get/set configuration |
| `cherry-pick` | `git cherry-pick <commit>` | Apply commit |
| `blame` | `git blame <file>` | Show who changed lines |

---

## Package Managers

### npm (15 subcommands)

| Subcommand | Syntax | Description |
|------------|--------|-------------|
| `install` | `npm install [package]` | Install dependencies |
| `uninstall` | `npm uninstall <package>` | Remove package |
| `update` | `npm update [package]` | Update packages |
| `run` | `npm run <script>` | Run package script |
| `start` | `npm start` | Run start script |
| `test` | `npm test` | Run tests |
| `build` | `npm run build` | Build project |
| `init` | `npm init` | Create package.json |
| `publish` | `npm publish` | Publish package |
| `list` | `npm list` | List installed packages |
| `outdated` | `npm outdated` | Check for updates |
| `audit` | `npm audit` | Security audit |
| `cache` | `npm cache <command>` | Manage cache |
| `link` | `npm link [package]` | Link local package |
| `version` | `npm version <type>` | Bump version |

### yarn (13 subcommands) ✨

| Subcommand | Syntax | Description |
|------------|--------|-------------|
| `install` | `yarn install [options]` | Install all dependencies |
| `add` | `yarn add <package>` | Add package |
| `remove` | `yarn remove <package>` | Remove package |
| `upgrade` | `yarn upgrade [package]` | Update packages |
| `run` | `yarn run <script>` | Run script |
| `test` | `yarn test` | Run tests |
| `init` | `yarn init` | Create package.json |
| `list` | `yarn list` | List packages |
| `cache` | `yarn cache <command>` | Manage cache |
| `workspaces` | `yarn workspaces <command>` | Manage monorepo |
| `why` | `yarn why <package>` | Show dependencies |
| `outdated` | `yarn outdated` | Check updates |
| `global` | `yarn global <command>` | Global packages |

### pip (13 subcommands)

| Subcommand | Syntax | Description |
|------------|--------|-------------|
| `install` | `pip install <package>` | Install package |
| `uninstall` | `pip uninstall <package>` | Remove package |
| `list` | `pip list` | List installed |
| `show` | `pip show <package>` | Show package info |
| `freeze` | `pip freeze` | Output requirements |
| `search` | `pip search <query>` | Search PyPI |
| `download` | `pip download <package>` | Download package |
| `wheel` | `pip wheel <package>` | Build wheel |
| `hash` | `pip hash <file>` | Compute hash |
| `check` | `pip check` | Verify dependencies |
| `config` | `pip config <command>` | Manage config |
| `cache` | `pip cache <command>` | Manage cache |
| `debug` | `pip debug` | Show debug info |

---

## Containers & Virtual Environments

### docker (18 subcommands)

| Subcommand | Syntax | Description |
|------------|--------|-------------|
| `run` | `docker run [options] <image>` | Run container |
| `build` | `docker build [options] <path>` | Build image |
| `pull` | `docker pull <image>` | Pull image |
| `push` | `docker push <image>` | Push image |
| `ps` | `docker ps [options]` | List containers |
| `stop` | `docker stop <container>` | Stop container |
| `start` | `docker start <container>` | Start container |
| `restart` | `docker restart <container>` | Restart container |
| `rm` | `docker rm <container>` | Remove container |
| `rmi` | `docker rmi <image>` | Remove image |
| `exec` | `docker exec [options] <container>` | Execute in container |
| `logs` | `docker logs <container>` | View logs |
| `images` | `docker images` | List images |
| `inspect` | `docker inspect <object>` | Show details |
| `compose` | `docker compose <command>` | Multi-container apps |
| `network` | `docker network <command>` | Manage networks |
| `volume` | `docker volume <command>` | Manage volumes |
| `prune` | `docker prune` | Remove unused data |

### venv (17 subcommands)

| Subcommand | Syntax | Description |
|------------|--------|-------------|
| `create` | `python -m venv <name>` | Create environment |
| `activate` | Platform-specific | Activate venv |
| `deactivate` | `deactivate` | Deactivate venv |
| `install` | `pip install <package>` | Install in venv |
| `list` | `pip list` | List venv packages |
| `freeze` | `pip freeze` | Export requirements |
| `remove` | `rm -rf venv/` | Delete venv |
| `which` | `which python` | Check active venv |
| `run` | `venv/Scripts/python script.py` | Run without activating |
| `upgrade` | `pip install --upgrade pip` | Upgrade pip |
| `requirements` | `pip install -r requirements.txt` | Install from file |
| `check` | Platform-specific check | Verify venv active |
| `path` | Platform-specific | Show venv path |
| `clone` | Copy requirements + recreate | Clone to new machine |
| `clean` | `pip uninstall -y -r` | Clean packages |
| `isolate` | Virtual environment creation | Isolate projects |
| `troubleshoot` | Various fixes | Fix common issues |

---

## Testing

### pytest (10 subcommands)

| Subcommand | Syntax | Description |
|------------|--------|-------------|
| `basic` | `pytest` | Run all tests |
| `verbose` | `pytest -v` | Verbose output |
| `specific` | `pytest test_file.py` | Run specific file |
| `keyword` | `pytest -k "pattern"` | Filter by keyword |
| `markers` | `pytest -m "marker"` | Run marked tests |
| `coverage` | `pytest --cov` | Test coverage |
| `parallel` | `pytest -n auto` | Parallel execution |
| `watch` | `pytest-watch` | Watch mode |
| `debug` | `pytest --pdb` | Debug on failure |
| `fixtures` | `pytest --fixtures` | List fixtures |

---

## Network & Remote

### curl (10 subcommands) ✨

| Subcommand | Syntax | Description |
|------------|--------|-------------|
| `get` | `curl [options] <URL>` | GET request |
| `post` | `curl -X POST [options] <URL>` | POST request |
| `put` | `curl -X PUT [options] <URL>` | PUT request |
| `delete` | `curl -X DELETE [options] <URL>` | DELETE request |
| `auth` | `curl [auth-options] <URL>` | Authentication |
| `headers` | `curl -H <header> <URL>` | Custom headers |
| `download` | `curl [download-options] <URL>` | Download files |
| `verbose` | `curl [verbose-options] <URL>` | Debug requests |
| `timeout` | `curl [timeout-options] <URL>` | Timeout control |
| `proxy` | `curl [proxy-options] <URL>` | Proxy settings |

**Quick Examples:**
```bash
curl https://api.github.com/users/octocat
curl -X POST -H "Content-Type: application/json" -d '{"key":"value"}' https://api.example.com
curl -u username:password https://api.example.com
curl -O https://example.com/file.zip
curl -L --max-time 30 https://example.com
```

### ssh (10 subcommands) ✨

| Subcommand | Syntax | Description |
|------------|--------|-------------|
| `connect` | `ssh [options] user@host` | Connect to server |
| `keygen` | `ssh-keygen [options]` | Generate keys |
| `copy-id` | `ssh-copy-id user@host` | Copy public key |
| `config` | Edit `~/.ssh/config` | Client configuration |
| `tunnel` | `ssh -L <local:dest:remote>` | Port forwarding |
| `scp` | `scp [options] source dest` | Secure copy |
| `agent` | `ssh-agent` / `ssh-add` | Key management |
| `jump` | `ssh -J jumphost user@dest` | Jump host |
| `known-hosts` | `ssh-keygen -R hostname` | Manage known hosts |
| `permissions` | `chmod <perms> <file>` | Fix permissions |

**Quick Examples:**
```bash
ssh user@example.com
ssh-keygen -t ed25519 -C "email@example.com"
ssh-copy-id user@example.com
ssh -L 8080:localhost:80 user@example.com
scp file.txt user@example.com:/path/
```

### localhost (15 subcommands)

| Subcommand | Syntax | Description |
|------------|--------|-------------|
| `kill-port` | Platform-specific | Kill process on port |
| `find-port` | Platform-specific | Find what's on port |
| `list-connections` | `netstat -ano` / `lsof` | List all connections |
| `kill-all` | Kill multiple servers | Kill all dev servers |
| `common-ports` | Reference guide | Common port numbers |
| Various port-specific commands | | Port 3000, 5000, 8000, 8080, etc. |

---

## Text Processing

### grep (10 subcommands) ✨

| Subcommand | Syntax | Description |
|------------|--------|-------------|
| `search` | `grep [options] pattern [file]` | Search patterns |
| `regex` | `grep -E "pattern" [file]` | Extended regex |
| `context` | `grep -A/-B/-C <num> pattern` | Context lines |
| `files` | `grep [file-options] pattern` | File operations |
| `count` | `grep -c pattern [file]` | Count matches |
| `invert` | `grep -v pattern [file]` | Invert match |
| `color` | `grep --color pattern` | Highlight matches |
| `multiple` | `grep -e pattern1 -e pattern2` | Multiple patterns |
| `quiet` | `grep -q pattern [file]` | Quiet mode |
| `binary` | `grep [binary-options] pattern` | Binary files |

**Quick Examples:**
```bash
grep "error" logfile.txt
grep -r "TODO" src/
grep -i "pattern" file.txt                    # Case-insensitive
grep -n "function" *.js                        # With line numbers
grep -A 3 "error" log.txt                      # 3 lines after
grep -E "error|warning" log.txt                # Multiple patterns
grep -r "pattern" --include="*.log" /var/log/  # Filter files
```

---

## Windows System

### powershell (22 subcommands)

| Command | Description |
|---------|-------------|
| `Get-Process` | List processes |
| `Stop-Process` | Kill process |
| `Get-Service` | List services |
| `Start-Service` | Start service |
| `Stop-Service` | Stop service |
| `Get-ChildItem` | List files (ls) |
| `Copy-Item` | Copy files |
| `Move-Item` | Move files |
| `Remove-Item` | Delete files |
| `New-Item` | Create file/dir |
| `Get-Content` | Read file |
| `Set-Content` | Write file |
| `Select-String` | Search text |
| `Get-NetTCPConnection` | Network connections |
| `Test-NetConnection` | Test connectivity |
| `Get-ExecutionPolicy` | Check execution policy |
| `Set-ExecutionPolicy` | Set execution policy |
| `Get-Help` | Get command help |
| `Get-Command` | List commands |
| `Get-Alias` | List aliases |
| `Where-Object` | Filter objects |
| `ForEach-Object` | Loop objects |

### cmd (20 subcommands)

| Command | Description |
|---------|-------------|
| `netstat` | Network statistics |
| `tasklist` | List processes |
| `taskkill` | Kill process |
| `ipconfig` | Network config |
| `ping` | Test connectivity |
| `tracert` | Trace route |
| `findstr` | Search text |
| `dir` | List directory |
| `cd` | Change directory |
| `copy` | Copy files |
| `move` | Move files |
| `del` | Delete files |
| `mkdir` | Create directory |
| `rmdir` | Remove directory |
| `type` | Display file |
| `echo` | Print text |
| `set` | Environment variables |
| `path` | Show/modify PATH |
| `cls` | Clear screen |
| `exit` | Exit command prompt |

---

## Linux System

### linux (30+ subcommands)

**File Operations:**
- `ls` - List directory contents
- `cd` - Change directory
- `pwd` - Print working directory
- `mkdir` - Make directory
- `rmdir` - Remove directory
- `cp` - Copy files
- `mv` - Move/rename files
- `rm` - Remove files
- `touch` - Create empty file
- `cat` - Display file contents
- `less` - Page through file
- `head` - Show file start
- `tail` - Show file end
- `find` - Search for files
- `locate` - Find files by name

**Text Processing:**
- `grep` - Search text patterns
- `sed` - Stream editor
- `awk` - Text processing
- `cut` - Cut columns
- `sort` - Sort lines
- `uniq` - Remove duplicates
- `wc` - Word count

**Process Management:**
- `ps` - Process status
- `top` - Process monitor
- `htop` - Interactive monitor
- `kill` - Terminate process
- `killall` - Kill by name
- `pkill` - Kill by pattern

**System:**
- `chmod` - Change permissions
- `chown` - Change owner
- `df` - Disk space
- `du` - Disk usage
- `free` - Memory usage
- `uname` - System info
- `uptime` - System uptime

**Archive:**
- `tar` - Archive files
- `gzip` - Compress files
- `gunzip` - Decompress files
- `zip` - Create zip
- `unzip` - Extract zip

**Network:**
- `curl` - Transfer data
- `wget` - Download files
- `ping` - Test connection
- `netstat` - Network stats
- `ss` - Socket statistics
- `ip` - Network config

**Services:**
- `systemctl` - Service manager
- `service` - Service control
- `journalctl` - System logs

---

## BashBot Features

### Special Commands

| Command | Description |
|---------|-------------|
| `bashbot list` | List all commands |
| `bashbot search <query>` | Search commands |
| `bashbot --history` | Recent command history |
| `bashbot --stats` | Most used commands |
| `bashbot --smart` | Context detection |
| `bashbot --copy <cmd>` | Copy to clipboard |
| `bashbot -l <cmd>` | List all flags |
| `bashbot -c <cmd>` | Generate cheat sheet |

### Interactive Mode Commands

```bash
python bashbot.py          # Start interactive mode
bashbot> list              # Show all commands
bashbot> search port       # Search commands
bashbot> flags docker      # Show all docker flags
bashbot> quick git         # Quick reference
bashbot> history           # Recent commands
bashbot> stats             # Most used
bashbot> smart             # Context detection
bashbot> git commit        # Command details
bashbot> exit              # Exit
```

---

## Command Count by Category

| Category | Commands | Subcommands |
|----------|----------|-------------|
| 🔄 Version Control | 1 | 21 |
| 📦 Package Managers | 3 | 41 |
| 🐳 Containers & Envs | 2 | 35 |
| 🧪 Testing | 1 | 10 |
| 🌐 Network & Remote | 3 | 35 |
| 📝 Text Processing | 1 | 10 |
| 🪟 Windows System | 2 | 42 |
| 🐧 Linux System | 1 | 30+ |
| **📊 TOTAL** | **14** | **224+** |

---

## Recent Additions (2025-11-30)

✨ **curl** - HTTP client, API testing, file downloads
✨ **yarn** - JavaScript package manager with workspaces
✨ **ssh** - Secure shell, keys, tunneling, file transfer
✨ **grep** - Pattern searching and text filtering

---

## Coming Soon

🔜 **kubectl** - Kubernetes cluster management
🔜 **make** - Build automation
🔜 **terraform** - Infrastructure as code
🔜 **aws** - AWS CLI commands
🔜 **jq** - JSON processor

---

## Usage Patterns

### Quick Lookups
```bash
bashbot git commit                    # Full documentation
bashbot --copy curl post              # Copy syntax
bashbot -l docker                     # All docker flags
```

### Discovery
```bash
bashbot list                          # All commands
bashbot search "port"                 # Find port commands
bashbot --smart                       # Project-specific suggestions
```

### Learning
```bash
bashbot -c git                        # Git cheat sheet
bashbot git                           # List git subcommands
bashbot --history                     # What you've used recently
```

---

## Contributing

Add new commands by creating JSON files in `commands/` directory:
```bash
commands/
├── git.json
├── curl.json
├── yarn.json
└── your-new-command.json
```

BashBot auto-loads all command files!

---

**📚 Full Documentation**: [README.md](README.md)
**⚡ Quick Start**: [QUICK_START.md](QUICK_START.md)
**📖 Command Files**: [commands/](commands/)

---

*Built with ❤️ to help developers remember command syntax*

**Never forget a flag again!** 🚀
