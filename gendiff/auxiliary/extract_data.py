import json
import yaml
from yaml.loader import SafeLoader
import os


def extract_data_from_file(first_file_path, second_file_path):
    filename_1, file_extension_1 = os.path.splitext(first_file_path)
    filename_2, file_extension_2 = os.path.splitext(second_file_path)

    if file_extension_1 == '.json' and file_extension_2 == '.json':
        data_file_1 = json.load(open(first_file_path))
        data_file_2 = json.load(open(second_file_path))
        extension = '.json'
        return data_file_1, data_file_2, extension
    elif file_extension_1 in ['.yml', '.yaml'] and file_extension_2 in ['.yml', '.yaml']:
        data_file_1 = yaml.load(open(first_file_path), Loader=SafeLoader)
        data_file_2 = yaml.load(open(second_file_path), Loader=SafeLoader)
        extension = '.yml'
        return data_file_1, data_file_2, extension