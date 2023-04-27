from Match import Match
from config import *

class Dictionary:
    def __init__(self, File, WORD_LENGTH: int = 5)->None:
        if type(WORD_LENGTH)!=int:
            raise ValueError(f'{WORD_LENGTH} have to be an integer')
        self.file = File
        self.words = self.file.getContentByLength(WORD_LENGTH)

    def reduceList(self, match:Match, position:int):
        if match.status == NOT_IN_THE_WORD:
            self.deleteWordsWithLetter(match.letter)
        if match.status == IN_WORD_BUT_BAD_POSITION:
            self.deleteWordsWithLetterInPosition(match.letter, position)
        if match.status == IN_WORD_AND_IN_PLACE:
            self.deleteWordsWithoutLetterInPosition(match.letter, position)

    def deleteWordsWithLetter(self, letter:str):
        self.words = [word for word in self.words if letter not in word]

    def deleteWordsWithLetterInPosition(self, letter:str, position:int):
        self.words = [word for word in self.words if letter in word and word[position] is not letter]
    
    def deleteWordsWithoutLetterInPosition(self, letter:str, position:int):
        self.words = [word for word in self.words if letter in word[position]]