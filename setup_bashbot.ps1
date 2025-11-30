# BashBot Global Access Setup Script
# Run this script to make BashBot available from anywhere in PowerShell

$bashbotPath = "C:\Users\William\OneDrive\Desktop\AppIdeas\bashCommands\bashbot.py"

Write-Host "=" * 60 -ForegroundColor Cyan
Write-Host "  BashBot Global Access Setup" -ForegroundColor Cyan
Write-Host "=" * 60 -ForegroundColor Cyan
Write-Host ""

# Check if bashbot.py exists
if (-not (Test-Path $bashbotPath)) {
    Write-Host "ERROR: bashbot.py not found at: $bashbotPath" -ForegroundColor Red
    Write-Host "Please update the path in this script." -ForegroundColor Red
    exit 1
}

# Get PowerShell profile path
$profilePath = $PROFILE

Write-Host "PowerShell Profile: $profilePath" -ForegroundColor Yellow
Write-Host ""

# Create profile if it doesn't exist
if (-not (Test-Path $profilePath)) {
    Write-Host "Creating PowerShell profile..." -ForegroundColor Green
    New-Item -Path $profilePath -ItemType File -Force | Out-Null
}

# Check if bashbot function already exists in profile
$profileContent = Get-Content $profilePath -Raw -ErrorAction SilentlyContinue
if ($profileContent -like "*function bb*") {
    Write-Host "WARNING: 'bb' function already exists in profile!" -ForegroundColor Yellow
    $overwrite = Read-Host "Do you want to overwrite it? (y/n)"
    if ($overwrite -ne 'y') {
        Write-Host "Setup cancelled." -ForegroundColor Yellow
        exit 0
    }
}

# Function to add to profile
$bashbotFunction = @"

# BashBot - Quick command reference helper
function bb {
    python "$bashbotPath" `$args
}

# BashBot aliases for common operations
function bbflags {
    python "$bashbotPath" -l `$args
}

function bbquick {
    python "$bashbotPath" `$args | Select-String -Pattern "QUICK REFERENCE" -Context 0,100
}

function bbcheat {
    python "$bashbotPath" -c `$args
}
"@

# Add function to profile
Add-Content -Path $profilePath -Value $bashbotFunction

Write-Host "SUCCESS! BashBot functions added to PowerShell profile!" -ForegroundColor Green
Write-Host ""
Write-Host "Available commands:" -ForegroundColor Cyan
Write-Host "  bb <command>           - Quick lookup (e.g., 'bb git commit')" -ForegroundColor White
Write-Host "  bbflags <command>      - Show all flags (e.g., 'bbflags taskkill')" -ForegroundColor White
Write-Host "  bbcheat <command>      - Generate cheat sheet (e.g., 'bbcheat git')" -ForegroundColor White
Write-Host ""
Write-Host "IMPORTANT: Restart PowerShell or run:" -ForegroundColor Yellow
Write-Host "  . `$PROFILE" -ForegroundColor White
Write-Host ""
Write-Host "Then try: bb git" -ForegroundColor Green
Write-Host "=" * 60 -ForegroundColor Cyan
