#!/bin/bash

# Get the directory where the script is located
script_dir=$(dirname "$0")

# Create the tarball, excluding specified files and directories
tar -zcvf "$script_dir/inspector_filtered.tar.gz" \
    --exclude '.DS_Store' \
    --exclude '.git' \
    --exclude '__pycache__' \
    --exclude 'venv' \
    --exclude '__init__.py' \
    --exclude '*.tar.gz' \
    .
