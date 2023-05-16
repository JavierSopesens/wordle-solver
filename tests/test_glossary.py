import pytest
from classes import Glossary
from config import WORD_LENGTH

mockWordList = ['break', 'bwana', 'cable', 'cache', 'cages', 'cagey', 'cakes', 'calls',
                'calms', 'camel', 'camps', 'canal', 'caper', 'carat', 'carbs', 'cares']


def test_glossary_no_arguments():
    with pytest.raises(TypeError):
        Glossary()


def test_glossary_empty_words():
    with pytest.raises(ValueError):
        Glossary([])


def test_reduceList_no_args():
    myGlossary = Glossary(mockWordList)
    with pytest.raises(TypeError):
        myGlossary.reduceList()


def test_reduceList_wrong_types():
    myGlossary = Glossary(mockWordList)
    with pytest.raises(TypeError):
        myGlossary.reduceList('a', 1, 1)
    with pytest.raises(TypeError):
        myGlossary.reduceList(1, 1, 1)
    with pytest.raises(TypeError):
        myGlossary.reduceList(1, 'a', 'a')


def test_reduceList_wrong_position():
    myGlossary = Glossary(mockWordList)
    with pytest.raises(IndexError):
        myGlossary.reduceList(2, 'b', -1)
    with pytest.raises(IndexError):
        myGlossary.reduceList(2, 'b', WORD_LENGTH + 1)


def test_reduceList_rigth_behavior():
    # assertions with status 0
    myGlossary = Glossary(mockWordList)
    myGlossary.reduceList(0, 'e', 2)
    assert myGlossary.words == ['bwana', 'calls',
                                'calms', 'camps', 'canal', 'carat', 'carbs']
    # assertions with status 1
    myGlossary = Glossary(mockWordList)
    myGlossary.reduceList(1, 'a', 1)
    assert myGlossary.words == ['break', 'bwana']
    # assertions with status 2
    myGlossary = Glossary(mockWordList)
    myGlossary.reduceList(2, 'm', 2)
    assert myGlossary.words == ['camel', 'camps']