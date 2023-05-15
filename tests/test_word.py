import pytest
from classes.Word import Word

def test_word_no_arg():
    with pytest.raises(ValueError):
        letters = []
        Word(letters)

def test_word_usual_behavior():
    letters = 'audio'
    word = Word(letters)
    assert word.letters == 'audio'

def test_word_containsLetter_more_than_one_letter():
    letters = 'audio'
    word = Word(letters)
    with pytest.raises(ValueError):
        print(len('aa'))
        word.containsLetter('aa')

def test_word_not_containsLetter():
    letters = 'audio'
    word = Word(letters)
    assert word.containsLetter('z') ==  False

def test_word_containsLetter():
    letters = 'audio'
    word = Word(letters)
    assert word.containsLetter('a') == True