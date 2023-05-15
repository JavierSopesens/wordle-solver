import pytest
from classes import File
from config import FILE_PATH

def test_no_args():
    with pytest.raises(TypeError):
        File()

def test_file_invalid_name():
    with pytest.raises(ValueError):
        File('invalid_path/invalid_file.txt')


def test_getContentByLength_wrong_type():
    myFile = File(FILE_PATH)
    with pytest.raises(ValueError):
        myFile.getContentByLength('a')

def test_getContentByLength_right_behavior():
    myFile = File('tests/mock_glossary.txt')
    assert myFile.getContentByLength(1) == []
    assert myFile.getContentByLength(4) == ['abba']
    assert myFile.getContentByLength(7) == ['abdomen','abandon']
