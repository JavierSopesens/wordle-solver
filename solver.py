from File import File

LETTER_NOT_EXIST = 0
LETTER_EXIST_IN_OTHER_POSITION = 1
LETTER_IN_PLACE = 2


def getInput() -> list:
    letters = input('print Letters \n')
    values = input('print Values \n')
    return list(zip(letters, values))


def reduceListOfWords(letter_value: tuple, words: list, position: int) -> list:
    letter = letter_value[0]
    status = int(letter_value[1])

    if status == LETTER_NOT_EXIST:
        outputWords = [word for word in words if letter_not_in_word(letter, word)]
    if status == LETTER_EXIST_IN_OTHER_POSITION:
        outputWords = [word for word in words if letter_in_word_in_different_position(letter, word, position)]
    if status == LETTER_IN_PLACE:
        outputWords = [word for word in words if letter_in_word_in_position(letter, word, position)]
    return outputWords


def letter_not_in_word(letter: str, word: list[str]) -> bool:
    return letter not in word


def letter_in_word_in_different_position(letter: str, word: list[str], position: int) -> bool:
    return letter in word and word[position] != letter


def letter_in_word_in_position(letter: str, word: list[str], position: int) -> bool:
    return word[position] == letter


def letterRepeated(currentLetter: str, word: list[str]) -> bool:
    currentChar = currentLetter[0]
    currentValue = currentLetter[1]
    wordChar = [letters[0] for letters in word]
    wordValues = [letters[1] for letters in word]

    timesRepeat = word.count(currentLetter)
    if timesRepeat != 1:
        i = 0
        for letter in wordChar:
            if letter == currentChar and currentValue < wordValues[i]:
                return True
            i += 1

    return False


def reduceRepeated(letter_value: tuple, words: list, position: int):
    # can be improved: in case 0-1,0-2,1-2
    return [word for word in words if letter_in_word_in_different_position(letter_value[0], word, position)]


File = File()
wordleWord = getInput()
print(File.getNumberOfWords())
count = 0
for letter_value in wordleWord:
    currentWords = File.getWords()
    repeated = letterRepeated(letter_value, wordleWord)
    if not repeated:
        newWords = reduceListOfWords(letter_value, currentWords, count)
    else:
        newWords = reduceRepeated(letter_value, currentWords, count)
    File.setWords(newWords)
    print(File.getNumberOfWords())
    count += 1