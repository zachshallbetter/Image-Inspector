
import sys
import os
from file_image_info import get_image_info

def process_directory(directory):
    # Initialize a list to hold file information dictionaries
    all_file_info = []

    # Walk through all files in the directory
    for root, _, files in os.walk(directory):
        for name in files:
            file_path = os.path.join(root, name)

            # Get the file information using our function
            file_info = get_image_info(file_path)

            # Add the information dictionary to our list
            all_file_info.append(file_info)

    # Return the list of file information dictionaries
    return all_file_info

if __name__ == '__main__':
    # If a command line argument is provided, use it as the directory. If not, use the current directory.
    directory = sys.argv[1] if len(sys.argv) > 1 else '.'

    all_file_info = process_directory(directory)
    for file_info in all_file_info:
        print(file_info)
