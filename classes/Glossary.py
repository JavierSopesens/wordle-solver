from config import MatchStatus as status
from classes.Word import Word

class Glossary:
    def __init__(self, words: list[str]) -> None:
        if not words:
            raise TypeError("words parameter were empty")
        self.words = words

    def reduceList(self, letter_status: int, letter_char: str, position:int):
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