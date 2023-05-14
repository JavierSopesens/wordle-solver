from dataclasses import dataclass

@dataclass
class Word:
    letters:list[str]

    def hasRepeatedLetters(self) -> bool:
        return any(self.letters.count(char) != 1 for char in self.letters) 
                
class Suggester():
    def __init__(self, words: list[str]) -> None:
        self.words = words
        self.timesLetterRepeated:dict = self.countTimesEveryLetterIsRepeated()
        self.wordScore:dict = self.sumWordScore()

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
        wordScore = {word:0 for word in self.words}

        for word in self.words:
            for char in word:
                wordScore[word] += self.timesLetterRepeated[char]
        return wordScore

    def sortWordsByScore(self) -> dict:
        return sorted(self.wordScore, key = self.wordScore.get, reverse = True)

    def getSpecificWords(self, originalWordsList, listWithRepeatedLetters: bool) -> list[str]:
        filteredWords = []
        for word in originalWordsList:
            word = Word(word)
            if word.hasRepeatedLetters() == listWithRepeatedLetters:
                filteredWords.append(word.letters)
        return filteredWords

    def recommendBestOption(self)->str:
        sortedWordsByScore = self.sortWordsByScore()
        wordsWithoutLettersRepeated = self.getSpecificWords(sortedWordsByScore, listWithRepeatedLetters = False)
        wordsWithLettersRepeated    = self.getSpecificWords(sortedWordsByScore, listWithRepeatedLetters = True)
        # print(f"length wordds w/o repeated:{len(wordsWithoutLettersRepeated)}")
        # print(f"length wordds w/ repeated:{len(wordsWithLettersRepeated)}")
        
        return wordsWithLettersRepeated[0] if not wordsWithoutLettersRepeated else wordsWithoutLettersRepeated[0]