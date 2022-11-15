import json
import yaml
import os


def get_data(file_path):
    _, format = os.path.splitext(os.path.normpath(file_path))
    with open(file_path) as file:
        return parse(file, format)


def parse(file, format):
    if format == ".json":
        return json.load(file)
    if format == ".yaml" or ".yml":
        return yaml.safe_load(file)
    raise ValueError(f"{format} - format not supported")
