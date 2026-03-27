import os
import logging
import re
from typing import List, Tuple

logger = logging.getLogger(__name__)

def is_valid_email(email: str) -> bool:
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return bool(re.match(pattern, email))

def convert_to_datetime(date_str: str, date_format: str) -> str:
    date_format_map = {
        'yyyy-MM-dd': '%Y-%m-%d',
        'MM/dd/yyyy': '%m/%d/%Y',
    }
    date_format = date_format_map.get(date_format, date_format)
    import datetime
    return datetime.datetime.strptime(date_str, date_format).strftime('%Y-%m-%d')

def remove_empty_lines(text: str) -> str:
    return '\n'.join([line for line in text.split('\n') if line.strip() != ''])

def get_json_data(json_str: str) -> dict:
    import json
    try:
        return json.loads(json_str)
    except json.JSONDecodeError as e:
        logger.error(f'Failed to parse JSON: {e}')
        return None

def get_files_in_dir(directory: str) -> List[str]:
    return sorted([f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))])

def get_dir_size(directory: str) -> int:
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(directory):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            total_size += os.path.getsize(fp)
    return total_size

def get_file_extension(file_name: str) -> str:
    return os.path.splitext(file_name)[1]