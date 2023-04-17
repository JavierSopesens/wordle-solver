import pytest
from main.Dictionary import Dictionary


def test_dict_empty_arguments():
    with pytest.raises(TypeError):
        Dictionary()


def test_dict_without_dict_file():
    with pytest.raises(TypeError):
        Dictionary(word_length=4)


def test_dict_length_not_integer():
    with pytest.raises(ValueError):
        Dictionary('es.txt', 3.14)


def test_bad_file_name():
    with pytest.raises(FileNotFoundError):
        Dictionary('espanol.txt')
