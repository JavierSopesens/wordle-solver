from config import WORD_LENGTH

class File:
    def __init__(self, name: str) -> None:
        self.name = name
        self.path = 'glossary/'+self.name

    def getContentByLength(self, word_length:int = WORD_LENGTH) ->list[str]:
        try:
            with open(self.path, encoding='utf-8') as file:
                return [word.rstrip() for word in file if len(word.rstrip()) == word_length]
        except FileNotFoundError:
            raise FileNotFoundError(f'File {self.name} not found')