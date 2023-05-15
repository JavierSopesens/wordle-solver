class Word:
    def __init__(self, letters: list[str]) -> None:
        if not (letters):
            raise ValueError('letters are necesary')
        self.letters = letters

    def containsLetter(self, letter: str) -> bool:
        if len(letter) != 1:
            raise ValueError('you only can pass one letter')
        return letter in self.letters

    def hasLetterInPlace(self, letter: str, place: int) -> bool:
        if place < 0 or place > len(self.letters):
            raise IndexError('place cannot be higher than number of letters in word')
        return letter in self.letters[place]

    def hasRepeatedLetters(self) -> bool:
        return len(set(self.letters)) < len(self.letters)