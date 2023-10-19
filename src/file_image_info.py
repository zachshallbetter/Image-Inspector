
import os
import pathlib
from PIL import Image
from datetime import datetime

def get_image_info(file_path):
    # Initialize a dictionary to hold file information
    file_info = {
        'FileName': None, 
        'FileSize': None, 
        'CreationDate': None, 
        'LastModifiedDate': None, 
        'Resolution': None, 
        'ColorSpace': None, 
        'Dimensions': None, 
        'NumberOfColors': None}

    # Check if the file path exists
    if not pathlib.Path(file_path).exists():
        print(f'File path does not exist: {file_path}')
        return file_info

    # Get the file information using os.path functions and update the dictionary
    file_info['FileName'] = os.path.basename(file_path)
    file_info['FileSize'] = os.path.getsize(file_path)

    # Get the file creation and modification dates and update the dictionary
    timestamp_creation = os.path.getctime(file_path)
    creation_date = datetime.fromtimestamp(timestamp_creation)
    file_info['CreationDate'] = creation_date.strftime('%Y-%m-%d %H:%M:%S')

    timestamp_modified = os.path.getmtime(file_path)
    modified_date = datetime.fromtimestamp(timestamp_modified)
    file_info['LastModifiedDate'] = modified_date.strftime('%Y-%m-%d %H:%M:%S')

    # Try to open image file using Pillow and get image information
    try:
        with Image.open(file_path) as img:
            # Update the dictionary with information about the image
            file_info['Resolution'] = img.info.get('dpi', 'unknown')
            file_info['ColorSpace'] = img.mode
            file_info['Dimensions'] = f'{img.width}x{img.height}'
            file_info['NumberOfColors'] = len(img.getcolors(maxcolors=256**3))
    except Exception as e:
        print(f'Failed to open {file_path} as an image. Reason: {str(e)}')

    return file_info
