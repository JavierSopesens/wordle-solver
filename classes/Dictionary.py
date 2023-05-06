from config import WORD_LENGTH, NOT_IN_THE_WORD, IN_WORD_BUT_BAD_POSITION, IN_WORD_AND_IN_PLACE
from . import Match, File

class Dictionary:
    def __init__(self, file:File, wordLength: int = WORD_LENGTH)->None:
        if type(wordLength)!=int:
            raise ValueError(f'{wordLength} have to be an integer')
        self.file = file
        self.words = self.file.getContentByLength(wordLength)

    def reduceList(self, match:Match, position:int) -> None:
        if match.status == NOT_IN_THE_WORD:
            self.deleteWordsWithLetter(match.letter)
        if match.status == IN_WORD_BUT_BAD_POSITION:
            self.deleteWordsWithLetterInPosition(match.letter, position)
        if match.status == IN_WORD_AND_IN_PLACE:
            self.deleteWordsWithoutLetterInPosition(match.letter, position)

    def deleteWordsWithLetter(self, letter:str) -> None:
        self.words = [word for word in self.words if letter not in word]

    def deleteWordsWithLetterInPosition(self, letter:str, position:int) -> None:
        self.words = [word for word in self.words if letter in word and word[position] is not letter]
    
    def deleteWordsWithoutLetterInPosition(self, letter:str, position:int) -> None:
        self.words = [word for word in self.words if letter in word[position]]