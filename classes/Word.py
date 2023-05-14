class Word:
    def __init__(self, letters:list[str]) -> None:
        self.letters = letters

    def containsLetter(self, letter:str) -> bool:
        return letter in self.letters
    
    def hasLetterInPlace(self, letter:str, place:int)->bool:
        return letter in self.letters[place]
    
    def hasRepeatedLetters(self)->bool:
        return len(set(self.letters)) < len(self.letters)