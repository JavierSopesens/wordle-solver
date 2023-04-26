from Match import Match
class Dictionary:
    def __init__(self, dict_file: str, word_length: int = 5)->None:
        if type(word_length)!=int:
            raise ValueError(f'{word_length} have to be an integer')
        self.dict_file = dict_file
        self.word_length = word_length
        self.words = self.fill(self.dict_file, self.word_length)

    def fill(self, dict_file: str, word_length: int):
        route = 'Dictionary/'+ dict_file
        try:
            with open(route, encoding='utf-8') as file:
                return [word.rstrip() for word in file if len(word.rstrip()) == word_length]
        except FileNotFoundError:
            raise FileNotFoundError(f'File {dict_file} not found')

    def reduceList(self, match:Match, position:int):
        NOT_IN_THE_WORD = 0
        IN_WORD_BUT_BAD_POSITION = 1
        IN_WORD_AND_IN_PLACE = 2

        if match.value == NOT_IN_THE_WORD:
            self.deleteWordsWithLetter(match.letter)
        if match.value == IN_WORD_BUT_BAD_POSITION:
            self.deleteWordsWithLetterInPosition(match.letter, position)
        if match.value == IN_WORD_AND_IN_PLACE:
            self.deleteWordsWithoutLetterInPosition(match.letter, position)

    def deleteWordsWithLetter(self, letter:str):
        self.words = [word for word in self.words if letter not in word]

    def deleteWordsWithLetterInPosition(self, letter:str, position:int):
        self.words = [word for word in self.words if letter in word and word[position] is not letter]
    
    def deleteWordsWithoutLetterInPosition(self, letter:str, position:int):
        self.words = [word for word in self.words if letter in word[position]]
        for word in self.words:
            if letter not in word[position]:
                self.words.remove(word)