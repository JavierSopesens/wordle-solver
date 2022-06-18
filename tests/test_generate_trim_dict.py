from main.generate_trim_dict import getAllWords
import pytest

def test_getAllWords_use_case()-> None:
    words =  getAllWords()
    assert type(words) == list
    assert len(words) != 0

def test_getAllWords_edge_case()->None:
    with pytest.raises(ValueError):
        getAllWords('random.txt')