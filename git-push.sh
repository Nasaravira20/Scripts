
#!/bin/bash

# Function to run a command and handle errors
run_command() {
    if ! "$@"; then
        echo "Error: Command '$*' failed."
        exit 1
    fi
}

# Function to stage all changes
git_add() {
    echo "Staging changes..."
    run_command git add .
}

# Function to commit changes with the given message
git_commit() {
    local message="$1"
    echo "Committing changes..."
    run_command git commit -m "$message"
}

# Function to pull the latest changes from the remote repository
git_pull() {
    echo "Pulling latest changes from origin main..."
    run_command git pull origin main
}

# Function to push committed changes to the remote repository
git_push() {
    echo "Pushing changes to origin main..."
    run_command git push origin main
}

# Main function
main() {
    if [ $# -lt 1 ]; then
        echo "Usage: $0 '<commit-message>'"
        exit 1
    fi

    local commit_message="$1"

    git_add
    git_commit "$commit_message"
    git_pull
    git_push
}

# Call the main function with all the script's arguments
main "$@"
