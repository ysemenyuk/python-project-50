import json
import yaml
import os


def get_data(file_path):
    full_file_path = os.path.join(os.path.abspath(os.getcwd()), file_path)
    _, format = os.path.splitext(file_path)
    with open(full_file_path) as file:
        return parse(file, format)


def parse(file, format):
    if format == ".json":
        return json.load(file)
    if format == ".yaml" or ".yml":
        return yaml.safe_load(file)
    raise ValueError(f"{format} - format not supported")
