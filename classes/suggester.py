from classes.Word import Word

class Suggester():
    def __init__(self, words: list[str]) -> None:
        self.words: list[str] = words
        self.timesLetterRepeated: dict = self.countTimesEveryLetterIsRepeated()
        self.wordScore: dict = self.sumWordScore()

    def countTimesEveryLetterIsRepeated(self) -> dict:
        timesLetterRepeated = {}
        for word in self.words:
            for char in word:
                if char not in timesLetterRepeated:
                    timesLetterRepeated[char] = 1
                else:
                    timesLetterRepeated[char] += 1
        return timesLetterRepeated

    def sumWordScore(self) -> dict:
        wordScore = {word: 0 for word in self.words}

        for word in self.words:
            for char in word:
                wordScore[word] += self.timesLetterRepeated[char]
        return wordScore

    def sortWordsByScore(self) -> dict:
        return sorted(self.wordScore, key=self.wordScore.get, reverse=True)

    def getSpecificWords(self, originalWordsList, listWithRepeatedLetters: bool) -> list[str]:
        filteredWords = []
        for word in originalWordsList:
            myWord = Word(word)
            if myWord.hasRepeatedLetters() == listWithRepeatedLetters:
                filteredWords.append(myWord.letters)
        return filteredWords

    def recommendBestOption(self) -> str:
        sortedWordsByScore = self.sortWordsByScore()
        wordsWithoutLettersRepeated = self.getSpecificWords(
            sortedWordsByScore, listWithRepeatedLetters=False)
        wordsWithLettersRepeated = self.getSpecificWords(
            sortedWordsByScore, listWithRepeatedLetters=True)

        return wordsWithLettersRepeated[0] if not wordsWithoutLettersRepeated else wordsWithoutLettersRepeated[0]
