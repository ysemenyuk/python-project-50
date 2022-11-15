import pytest
import os
from gendiff.generate_diff import generate_diff


f1_json = os.path.join(os.path.dirname(__file__), 'fixtures', 'file1.json')
f2_json = os.path.join(os.path.dirname(__file__), 'fixtures', 'file2.json')
f1_yml = os.path.join(os.path.dirname(__file__), 'fixtures', 'file1.yml')
f2_yml = os.path.join(os.path.dirname(__file__), 'fixtures', 'file2.yml')
expexted = os.path.join(os.path.dirname(__file__), 'fixtures', 'expected.txt')

def test_gendiff_json():
    with open(expexted) as answer:
        assert generate_diff(f1_json, f2_json) == answer.read()

def test_gendiff_yml():
    with open(expexted) as answer:
        assert generate_diff(f1_yml, f2_yml) == answer.read()

def test_parse():
    with pytest.raises(Exception):
        generate_diff(f1_json, "wrong_file_path")
