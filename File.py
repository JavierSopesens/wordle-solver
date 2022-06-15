def getFileName():
    from datetime import datetime
    date = datetime.today().strftime('%Y-%m-%d')
    return date + '.txt'


def importContent() -> list:
    with open('Dictionary/trimedDictionary.txt', 'r') as fullWordsList:
        words = [word for word in fullWordsList]
        return words


def generateFile(name: str, content: list[str]):
    with open(name, 'w') as file:
        for word in content:
            file.write(word)


class File:
    def __init__(self):
        from os.path import exists
        self.name = getFileName()
        if not exists(self.name):
            self.content = importContent()
            generateFile(self.name, self.content)

    def getWords(self) -> list[str]:
        with open(self.name) as document:
            return(document.readlines())

    def getNumberOfWords(self) -> int:
        return len(self.getWords())

    def setWords(self, words: list[str]):
        with open(self.name, 'w') as file:
            file.write(''.join(words))
