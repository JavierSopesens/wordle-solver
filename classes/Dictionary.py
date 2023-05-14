from config import MatchStatus as status

class Dictionary:
    def __init__(self, words: list[str]) -> None:
        if not words:
            raise TypeError("words parameter were empty")
        self.words = words

    def reduceList(self, letter_status: int, letter_char: str, position: int) -> None:
        if letter_status == status.NOT_IN_WORD.value:
            self.deleteWordsWithLetter(letter_char)
        if letter_status == status.IN_WORD_BUT_BAD_PLACE.value:
            self.deleteWordsWithLetterInPosition(letter_char, position)
        if letter_status == status.IN_WORD_AND_IN_PLACE.value:
            self.deleteWordsWithoutLetterInPosition(letter_char, position)

    def deleteWordsWithLetter(self, letter: str) -> None:
        self.words = [word for word in self.words if letter not in word]

    def deleteWordsWithLetterInPosition(self, letter: str, position: int) -> None:
        self.words = [word for word in self.words if letter in word and word[position] is not letter]

    def deleteWordsWithoutLetterInPosition(self, letter: str, position: int) -> None:
        self.words = [word for word in self.words if letter in word[position]]