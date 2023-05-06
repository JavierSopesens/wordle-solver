import pytest
from classes.File import File
from config import *

def test_no_args():
    with pytest.raises(TypeError):
        File()

def test_name_is_int():
    with pytest.raises(TypeError):
        File(1)

def test_getContent_file_not_exists():
    with pytest.raises(FileNotFoundError):
        myFile = File('and.txt')
        myFile.getContentByLength(WORD_LENGTH)
