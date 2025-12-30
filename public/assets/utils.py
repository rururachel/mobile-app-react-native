import json
import os
import re
import shutil
import sys
from datetime import datetime

def load_json(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

def write_json(file_path, data):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)

def delete_file(file_path):
    try:
        os.remove(file_path)
    except FileNotFoundError:
        pass

def create_folder(folder_path):
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

def get_file_extension(file_name):
    return os.path.splitext(file_name)[1].replace('.', '')

def get_file_size(file_path):
    return os.path.getsize(file_path)

def get_current_date():
    return datetime.now().strftime('%Y-%m-%d %H:%M:%S')

def is_email_valid(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))

def copy_file(src, dst):
    shutil.copy2(src, dst)

def is_file_exists(file_path):
    return os.path.exists(file_path)

def is_int(num):
    try:
        int(num)
        return True
    except ValueError:
        return False