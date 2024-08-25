
#!/usr/bin/env python

import subprocess
import sys

def run_command(command):
    """Runs a shell command and handles errors."""
    try:
        result = subprocess.run(command, check=True, text=True, capture_output=True)
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Error: Command '{' '.join(command)}' failed with error:\n{e.stderr}")
        sys.exit(1)

def git_add():
    """Stage all changes."""
    print("Staging changes...")
    run_command(['git', 'add', '.'])

def git_commit(message):
    """Commit changes with the given message."""
    print("Committing changes...")
    run_command(['git', 'commit', '-m', message])

def git_pull():
    """Pull the latest changes from the remote repository."""
    print("Pulling latest changes from origin main...")
    run_command(['git', 'pull', 'origin', 'main'])

def git_push():
    """Push committed changes to the remote repository."""
    print("Pushing changes to origin main...")
    run_command(['git', 'push', 'origin', 'main'])

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 git_auto.py '<commit-message>'")
        sys.exit(1)

    commit_message = sys.argv[1]

    git_add()
    git_commit(commit_message)
    git_pull()
    git_push()

if __name__ == "__main__":
    main()
