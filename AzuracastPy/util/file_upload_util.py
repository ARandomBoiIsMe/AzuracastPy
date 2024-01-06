import base64
import os

def generate_file_upload_structure(path: str, file: str):
    if not os.path.isfile(file):
        raise ValueError("File does not exist.")
    
    contents = None
    with open(file, 'rb') as f:
        contents = f.read()

    contents = base64.b64encode(contents)

    return {
        "path": path,
        "file": contents
    }