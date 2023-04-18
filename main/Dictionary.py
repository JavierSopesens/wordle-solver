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

    def reduceList(self, letter:str, value:int, position:int):
        # falta escribir toda la documentacion y test de esto
        NOT_IN_THE_WORD = 0
        IN_WORD_BUT_BAD_POSITION = 1
        IN_WORD_AND_IN_PLACE = 2

        if value == NOT_IN_THE_WORD:
            self.deleteWordsWithLetter(letter)
        if value == IN_WORD_BUT_BAD_POSITION:
            self.deleteWordsWithLetterInPosition(letter, position)
        if value == IN_WORD_AND_IN_PLACE:
            self.deleteWordsWithoutLetter(letter, position)

    def deleteWordsWithLetter(self, letter:str):
        for word in self.words:
            if letter in word:
                self.words.remove(word)

    def deleteWordsWithLetterInPosition(self, letter:str, position:int):
        # esta funcion parece fallar bajo audio - 10020
        for word in self.words:
            if letter not in word and word[position] is letter:
                self.words.remove(word)
    
    def deleteWordsWithoutLetter(self, letter:str, position:int):
        for word in self.words:
            if letter not in word[position]:
                self.words.remove(word)