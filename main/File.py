class File:
    def __init__(self, name: str) -> None:
        self.name = name
        self.path = 'Dictionary/'+self.name

    def getContentByLength(self, WORD_LENGTH:int) ->list[str]:
        try:
            with open(self.path, encoding='utf-8') as file:
                return [word.rstrip() for word in file if len(word.rstrip()) == WORD_LENGTH]
        except FileNotFoundError:
            raise FileNotFoundError(f'File {self.name} not found')