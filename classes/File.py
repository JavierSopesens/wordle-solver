from os import path

class File:
    def __init__(self, file_path: str) -> None:
        if not path.isfile(file_path):
            raise ValueError('file does not exists')
        self.path = file_path

    def getContentByLength(self, word_length:int) ->list[str]:
        try:
            if type(word_length)!=int:
                raise ValueError(f'{word_length} have to be an integer')
            with open(self.path, encoding='utf-8') as file:
                return [word.rstrip() for word in file if len(word.rstrip()) == word_length]
        except FileNotFoundError:
            raise FileNotFoundError(f'File {self.name} not found')