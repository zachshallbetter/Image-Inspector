#!/bin/bash

# Get the directory where the script is located
script_dir=$(dirname "$0")

# Get the last commit id
commit_id=$(git rev-parse --short HEAD)

# Define the project name
project_name="inspector"

# Define the output filename
output_filename="${project_name}-${commit_id}.tar.gz"

# Read .gitignore and exclude those files/directories while creating the tarball
tar -zcvf "$script_dir/$output_filename" \
    --exclude-vcs \
    --exclude-from "$script_dir/../.gitignore" \
    .
