import pytest
import os
from gendiff.generate_diff import generate_diff


f1_path = os.path.join(os.path.dirname(__file__), 'fixtures', 'file1.json')
f2_path = os.path.join(os.path.dirname(__file__), 'fixtures', 'file2.json')
expexted_path = os.path.join(os.path.dirname(__file__), 'fixtures', 'expected.txt')

def test_gendiff():
    with open(expexted_path) as answer:
        assert generate_diff(f1_path, f2_path) == answer.read()

def test_parse():
    with pytest.raises(Exception):
        generate_diff(f1_path, "wrong_file_path")
