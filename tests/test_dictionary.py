import pytest
from classes import Dictionary, File
from config import DICTIONARY_FILE, WORD_LENGTH


def test_dict_no_arguments():
    with pytest.raises(TypeError):
        Dictionary()

def test_dict_empty_words():
    with pytest.raises(TypeError):
        Dictionary()

def test_reduceList_no_args():
    pass
    # myFile = File(DICTIONARY_FILE)
    # myDict = myFile.getContentByLength(WORD_LENGTH)
    # myDict.reduceList()

def test_reduceList_letterStatus_wrong_type():
    pass

def test_reduceList_letter_char_wrong_type():
    pass

def test_reduceList_letter_position_type():
    pass

def test_reduceList_rigth_behavior():
    pass