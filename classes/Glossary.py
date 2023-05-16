from config import MatchStatus as status
from config import WORD_LENGTH
from classes.Word import Word

class Glossary:
    def __init__(self, words: list[str]) -> None:
        if not words:
            raise ValueError("words parameter were empty")
        self.words = words

    def reduceList(self, letter_status: int, letter_char: str, position: int):
        if not isinstance(letter_status, int) or not isinstance(letter_char, str) or not isinstance(position, int):
            raise TypeError("wrong types passed")
        if position < 0 or position > WORD_LENGTH:
            raise IndexError('invalid value for postion')
        
        trimmedList = []
        for word in self.words:
            myWord = Word(word)
            if letter_status is status.NOT_IN_WORD.value:
                if not myWord.containsLetter(letter_char):
                    trimmedList.append(word)
            if letter_status is status.IN_WORD_BUT_BAD_PLACE.value:
                if myWord.containsLetter(letter_char) and not myWord.hasLetterInPlace(letter_char, position):
                    trimmedList.append(word)
            if letter_status is status.IN_WORD_AND_IN_PLACE.value:
                if myWord.containsLetter(letter_char) and myWord.hasLetterInPlace(letter_char, position):
                    trimmedList.append(word)

        self.words = trimmedList