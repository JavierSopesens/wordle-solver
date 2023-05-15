import pytest
from classes.Word import Word


def test_word_no_arg() -> None:
    with pytest.raises(ValueError):
        letters = []
        Word(letters)


def test_word_usual_behavior() -> None:
    word = Word(letters='audio')
    assert word.letters == 'audio'


def test_word_containsLetter_more_than_one_letter() -> None:
    word = Word(letters='audio')
    with pytest.raises(ValueError):
        print(len('aa'))
        word.containsLetter('aa')


def test_word_not_containsLetter() -> None:
    word = Word(letters='audio')
    assert word.containsLetter('z') == False


def test_word_containsLetter() -> None:
    word = Word(letters='audio')
    assert word.containsLetter('a') == True

def test_word_hasLetterInPlace_place_out_of_range() -> None:
    word = Word(letters='audio')
    with pytest.raises(IndexError):
        word.hasLetterInPlace('a', 10)

def test_word_hasLetterInPlce() -> None:
    word = Word(letters='audio')
    assert word.hasLetterInPlace('a', 0) == True


def test_word_not_hasLetterInPlace() -> None:
    word = Word(letters='audio')
    assert word.hasLetterInPlace('z', 0) == False


def test_word_hasRepeatedletters() -> None:
    word = Word(letters='audio')
    assert word.hasRepeatedLetters() == False


def test_word_not_hasRepeatedletters() -> None:
    word = Word(letters='abacus')
    assert word.hasRepeatedLetters() == True
