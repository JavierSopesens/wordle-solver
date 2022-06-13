def getFileName():
    from datetime import datetime
    date = datetime.today().strftime('%Y-%m-%d')
    return date + '.txt'

def importContent():
    with open('five_char_words.txt', 'r') as fullWordsList:
        words = [word for word in fullWordsList]
        return words

def generateFile(name, content):
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

    def getWords(self):
        with open(self.name) as document:
            return(document.readlines())
    
    def getNumberOfWords(self):
        return len(self.getWords())

    def setWords(self, words):
        with open(self.name, 'w') as file:
            file.write(''.join(words))