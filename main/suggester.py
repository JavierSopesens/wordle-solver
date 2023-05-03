from dataclasses import dataclass

@dataclass
class Word:
    letters:list[str]

    @classmethod
    def hasRepeatedLetters(self) -> bool:
        repeated = False
        for char in self.letters:
            if self.letters.count(char) != 1:
                repeated = True
        return repeated
                
class Suggester():
    def __init__(self, Dictionary):
        self.words = Dictionary.words
        self.timesLetterRepeated:dict = {}
        self.wordScore:dict = {}

    def countTimesEveryLetterIsRepeated(self):
        for word in self.words:
            for char in word:
                if char not in self.timesLetterRepeated:
                    self.timesLetterRepeated[char] = 1
                else:
                    self.timesLetterRepeated[char] += 1

    def sumWordScore(self):
        for word in self.words:
            self.wordScore[word] = 0

        for word in self.words:
            for char in word:
                self.wordScore[word] += self.timesLetterRepeated[char]

    def sortWordsByScore(self):
        return sorted(self.wordScore, key = self.wordScore.get, reverse = True)

    def getSpecificWords(self, originalWordsList, listWithRepeatedLetters: bool = False):
        filteredWords = []
        for word in originalWordsList:
            word = Word(word)
            if word.hasRepeatedLetters() == listWithRepeatedLetters:
                filteredWords.append(word.letters)
        return filteredWords

    def recommendBestOption(self)->str:
        sortedWordsByScore = self.sortWordsByScore()
        wordsWithoutLettersRepeated = self.getSpecificWords(originalWordsList = sortedWordsByScore, listWithRepeatedLetters = False)
        wordsWithLettersRepeated = self.getSpecificWords(originalWordsList = sortedWordsByScore, listWithRepeatedLetters = True)

        return wordsWithLettersRepeated[0] if not wordsWithoutLettersRepeated else wordsWithoutLettersRepeated[0]