import pytest
from classes import Glossary, File
from config import FILE_PATH, WORD_LENGTH


def test_glossary_no_arguments():
    with pytest.raises(TypeError):
        Glossary()

def test_glossary_empty_words():
    with pytest.raises(TypeError):
        Glossary()

def test_reduceList_no_args():
    pass
    # myFile = File(FILE_PATH)
    # myGlossary = myFile.getContentByLength(WORD_LENGTH)
    # myGlossary.reduceList()

def test_reduceList_letterStatus_wrong_type():
    pass

def test_reduceList_letter_char_wrong_type():
    pass

def test_reduceList_letter_position_type():
    pass

def test_reduceList_rigth_behavior():
    pass