from config import WORD_LENGTH

class File:
    def __init__(self, name: str) -> None:
        self.name = name
        self.path = 'glossary/'+self.name

    def getContentByLength(self, word_length:int = WORD_LENGTH) ->list[str]:
        try:
            if type(word_length)!=int:
                raise ValueError(f'{word_length} have to be an integer')
            with open(self.path, encoding='utf-8') as file:
                return [word.rstrip() for word in file if len(word.rstrip()) == word_length]
        except FileNotFoundError:
            raise FileNotFoundError(f'File {self.name} not found')