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
                self.words = [word.rstrip() for word in file if len(word.rstrip()) == word_length]
        except FileNotFoundError:
            raise FileNotFoundError(f'File {dict_file} not found')
