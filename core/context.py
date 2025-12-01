"""
Context detection module for BashBot
Detects project type based on current directory contents
"""

import os
from pathlib import Path
from typing import List, Dict


class ContextDetector:
    """Detects project context based on directory contents"""

    # File patterns that indicate project type
    CONTEXT_PATTERNS = {
        'git': ['.git'],
        'npm': ['package.json', 'node_modules'],
        'python': ['requirements.txt', 'setup.py', 'pyproject.toml', 'Pipfile'],
        'venv': ['venv', '.venv', 'env', '.env'],
        'docker': ['Dockerfile', 'docker-compose.yml', 'docker-compose.yaml'],
        'pytest': ['pytest.ini', 'tests', 'test'],
        'pip': ['requirements.txt', 'setup.py'],
    }

    # Suggested commands for each context
    CONTEXT_SUGGESTIONS = {
        'git': [
            ('git status', 'Check repository status'),
            ('git log', 'View commit history'),
            ('git diff', 'See uncommitted changes'),
            ('git branch', 'List and manage branches'),
        ],
        'npm': [
            ('npm install', 'Install dependencies'),
            ('npm run', 'Run package scripts'),
            ('npm test', 'Run tests'),
            ('npm start', 'Start development server'),
        ],
        'python': [
            ('pip install', 'Install Python packages'),
            ('pip freeze', 'List installed packages'),
            ('python', 'Run Python scripts'),
        ],
        'venv': [
            ('venv activate', 'Activate virtual environment'),
            ('venv deactivate', 'Deactivate virtual environment'),
            ('venv install', 'Install packages in venv'),
            ('venv create', 'Create new virtual environment'),
        ],
        'docker': [
            ('docker build', 'Build Docker image'),
            ('docker run', 'Run Docker container'),
            ('docker ps', 'List running containers'),
            ('docker compose', 'Manage multi-container apps'),
        ],
        'pytest': [
            ('pytest', 'Run Python tests'),
            ('pytest verbose', 'Run tests with verbose output'),
            ('pytest coverage', 'Run tests with coverage'),
        ],
        'pip': [
            ('pip install', 'Install Python packages'),
            ('pip list', 'List installed packages'),
            ('pip freeze', 'Export requirements'),
        ],
    }

    def __init__(self, path: str = None):
        """
        Initialize context detector

        Args:
            path: Directory path to analyze. Defaults to current directory.
        """
        self.path = Path(path) if path else Path.cwd()

    def detect_contexts(self) -> List[str]:
        """
        Detect all contexts that apply to current directory

        Returns:
            List of detected context names (e.g., ['git', 'npm', 'python'])
        """
        detected = []

        for context_name, patterns in self.CONTEXT_PATTERNS.items():
            for pattern in patterns:
                check_path = self.path / pattern
                if check_path.exists():
                    detected.append(context_name)
                    break  # Don't check other patterns for this context

        return detected

    def get_suggestions(self, context_name: str = None) -> List[tuple]:
        """
        Get command suggestions for a specific context or all detected contexts

        Args:
            context_name: Specific context to get suggestions for. If None, get all.

        Returns:
            List of (command, description) tuples
        """
        if context_name:
            return self.CONTEXT_SUGGESTIONS.get(context_name, [])

        # Get suggestions for all detected contexts
        detected = self.detect_contexts()
        suggestions = []

        for context in detected:
            context_suggestions = self.CONTEXT_SUGGESTIONS.get(context, [])
            suggestions.extend(context_suggestions)

        return suggestions

    def format_context_report(self) -> str:
        """
        Format a readable report of detected contexts and suggestions

        Returns:
            Formatted string with context information
        """
        detected = self.detect_contexts()

        if not detected:
            return "No specific project context detected in current directory."

        report_lines = []
        report_lines.append("\n" + "=" * 60)
        report_lines.append("DETECTED PROJECT CONTEXTS")
        report_lines.append("=" * 60)
        report_lines.append(f"Directory: {self.path}")
        report_lines.append(f"Contexts: {', '.join(detected)}")
        report_lines.append("")

        for context in detected:
            report_lines.append(f"\n{context.upper()} - Suggested Commands:")
            report_lines.append("-" * 60)

            suggestions = self.CONTEXT_SUGGESTIONS.get(context, [])
            for cmd, desc in suggestions:
                report_lines.append(f"  {cmd:30}  # {desc}")

        report_lines.append("\n" + "=" * 60)
        report_lines.append("Tip: Use 'bashbot <command>' for detailed help")
        report_lines.append("=" * 60)

        return '\n'.join(report_lines)
