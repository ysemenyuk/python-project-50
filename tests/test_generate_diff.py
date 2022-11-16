import pytest
import os
from gendiff.generate_diff import generate_diff


f1_json = os.path.join(os.path.dirname(__file__), 'fixtures', 'file1.json')
f2_json = os.path.join(os.path.dirname(__file__), 'fixtures', 'file2.json')

f1_yml = os.path.join(os.path.dirname(__file__), 'fixtures', 'file1.yml')
f2_yml = os.path.join(os.path.dirname(__file__), 'fixtures', 'file2.yml')

expexted_stylish = os.path.join(os.path.dirname(__file__), 'fixtures', 'expected_stylish.txt')
expexted_json = os.path.join(os.path.dirname(__file__), 'fixtures', 'expected_json.txt')

def test_gendiff_json_formatter():
    with open(expexted_json) as f:
        expected = f.read()
        assert generate_diff(f1_json, f2_json, 'json') == expected
        assert generate_diff(f1_yml, f2_yml, 'json') == expected

def test_gendiff_stylish_formatter():
    with open(expexted_stylish) as f:
        expected = f.read()
        assert generate_diff(f1_json, f2_json) == expected
        assert generate_diff(f1_yml, f2_yml) == expected

def test_parse_files_paths():
    with pytest.raises(Exception):
        generate_diff(f1_json, "wrong_file_path")
