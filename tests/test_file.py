import pytest
from classes import File

def test_no_args():
    with pytest.raises(TypeError):
        File()

def test_invalid_name():
    with pytest.raises(ValueError):
        File('invalid_path/invalid_file.txt')