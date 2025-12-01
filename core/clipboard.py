"""
Clipboard utility module for BashBot
Copies text to clipboard using platform-specific commands
"""

import subprocess
import platform
import sys


def copy_to_clipboard(text: str) -> bool:
    """
    Copy text to clipboard using platform-specific commands

    Args:
        text: Text to copy to clipboard

    Returns:
        True if successful, False otherwise
    """
    system = platform.system()

    try:
        if system == 'Windows':
            # Use Windows clip command
            process = subprocess.Popen(['clip'], stdin=subprocess.PIPE, shell=True)
            process.communicate(input=text.encode('utf-8'))
            return process.returncode == 0

        elif system == 'Darwin':
            # Use macOS pbcopy command
            process = subprocess.Popen(['pbcopy'], stdin=subprocess.PIPE)
            process.communicate(input=text.encode('utf-8'))
            return process.returncode == 0

        elif system == 'Linux':
            # Try xclip first, then xsel as fallback
            try:
                process = subprocess.Popen(['xclip', '-selection', 'clipboard'],
                                         stdin=subprocess.PIPE)
                process.communicate(input=text.encode('utf-8'))
                return process.returncode == 0
            except FileNotFoundError:
                # Try xsel as fallback
                process = subprocess.Popen(['xsel', '--clipboard', '--input'],
                                         stdin=subprocess.PIPE)
                process.communicate(input=text.encode('utf-8'))
                return process.returncode == 0

        else:
            # Unsupported platform
            return False

    except Exception:
        return False


def is_clipboard_available() -> bool:
    """
    Check if clipboard functionality is available on this system

    Returns:
        True if clipboard is available, False otherwise
    """
    system = platform.system()

    if system == 'Windows':
        # clip is always available on Windows
        return True

    elif system == 'Darwin':
        # pbcopy is always available on macOS
        return True

    elif system == 'Linux':
        # Check if xclip or xsel is installed
        try:
            subprocess.run(['which', 'xclip'], capture_output=True, check=True)
            return True
        except (subprocess.CalledProcessError, FileNotFoundError):
            try:
                subprocess.run(['which', 'xsel'], capture_output=True, check=True)
                return True
            except (subprocess.CalledProcessError, FileNotFoundError):
                return False

    return False
