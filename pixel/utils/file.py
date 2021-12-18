import os
import hashlib


def md5_file(file_path) -> str:
    if os.path.exists(file_path) is False:
        raise FileNotFoundError("File not found: " + file_path)

    with open(file_path, 'rb') as f:
        return hashlib.md5(f).hexdigest()
