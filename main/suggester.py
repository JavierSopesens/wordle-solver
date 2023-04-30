from Dictionary import Dictionary

# estudiar si suggester deberia heredar o pasarlo por parametro del __init__

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

    def recommendBestOption(self):
        # sort words by value
        sortedWordsByScore = sorted(self.wordScore, key=self.wordScore.get, reverse=True)

        # divide words between if they have repeated letters or not
        wordsWithoutLettersRepeated: list = []
        wordsWithLettersRepeated: list = []
        hasRepeatedLetters = False

        for word in sortedWordsByScore:
            for char in word:
                if word.count(char) != 1:
                    hasRepeatedLetters = True
                    break
            if hasRepeatedLetters:
                wordsWithLettersRepeated.append(word)
            else:
                wordsWithoutLettersRepeated.append(word)
            hasRepeatedLetters = False

        # return better option
        if not wordsWithoutLettersRepeated:
            return wordsWithLettersRepeated[0]
        else:
            return wordsWithoutLettersRepeated[0]