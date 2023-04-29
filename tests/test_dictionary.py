import pytest
from main.Dictionary import Dictionary
from main.File import File
from main.Match import Match


def test_dict_empty_arguments():
    with pytest.raises(NameError):
        Dictionary()


def test_dict_without_dict_file():
    with pytest.raises(TypeError):
        Dictionary(word_length=4)


def test_dict_length_not_integer():
    with pytest.raises(ValueError):
        myFile = File('es.txt')
        Dictionary(myFile, 3.14)

def test_reduce_list_no_args():
    pass

def test_reduce_list_no_match():
    pass

def test_reduce_list_no_position():
    pass

def test_reduce_list_match_bad_type():
    pass

def test_reduce_list_position_not_int():
    pass