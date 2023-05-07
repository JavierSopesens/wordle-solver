from config import MatchStatus

class Dictionary:
    def __init__(self, words:list[str])->None:
        self.words = words

    def reduceList(self, letter_status:int, letter_char:str, position:int) -> None:
        if letter_status == MatchStatus.NOT_IN_THE_WORD:
            self.deleteWordsWithLetter(letter_char)
        if letter_status == MatchStatus.IN_WORD_BUT_BAD_POSITION:
            self.deleteWordsWithLetterInPosition(letter_char, position)
        if letter_status == MatchStatus.IN_WORD_AND_IN_PLACE:
            self.deleteWordsWithoutLetterInPosition(letter_char, position)

    def deleteWordsWithLetter(self, letter:str) -> None:
        self.words = [word for word in self.words if letter not in word]

    def deleteWordsWithLetterInPosition(self, letter:str, position:int) -> None:
        self.words = [word for word in self.words if letter in word and word[position] is not letter]
    
    def deleteWordsWithoutLetterInPosition(self, letter:str, position:int) -> None:
        self.words = [word for word in self.words if letter in word[position]]