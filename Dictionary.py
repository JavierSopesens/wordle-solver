class Dictionary:
    def __init__(self, file):
        self.file = file

    def getContent(self):
        with open(self.file) as file:
            return(file.readlines())
    
    def getNumberOfWords(self):
        return len(self.getContent())
    
    def setContent(self, content):
        with open(self.file, 'w') as file:
            file.write(content)