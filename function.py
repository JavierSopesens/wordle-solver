wordleWord = [['a', 'u', 'd', 'i', 'o'], [0, 0, 0, 0, 2]]

LETTER_NOT_EXIST = 0
LETTER_EXIST_IN_OTHER_POSITION = 1
LETTER_IN_PLACE = 2

def deleteWords(wordleWord):
    file = createFile()
    count = 0
    letters = wordleWord[0]
    values = wordleWord[1]

    printNumberOfWords(file)
    for letter in letters:
        letterStatus = wordleWord[1][count]
        WordsInFile = getWordsInFile(file)
        evaluated = evaluateRepeatedLetters(WordsInFile, file, count, letter, letters, values)
        if not evaluated:
            remainingWords = reduceListOfWords(letterStatus, WordsInFile, letter, count)
            writeWordsInFile(file, remainingWords)
        printNumberOfWords(file)
        count += 1
    # import os
    # os.remove(file)

def reduceListOfWords(status, WordsInFile, letter, position):
    remainingWords = ''
    for word in WordsInFile:
        if status == LETTER_NOT_EXIST:
            remainingWords += get_word_with_letter(word, letter)
        if status == LETTER_EXIST_IN_OTHER_POSITION:
            remainingWords += get_word_without_letter_and_with_letter_in_position(word, letter, position)
        if status == LETTER_IN_PLACE:
            remainingWords += get_word_without_letter_in_that_position(word, letter, position)
    return remainingWords

def evaluateRepeatedLetters(wordsInFile, file, position, analizedLetter, letters, values):
    # la variable file passa por aquí simplemente para ser un parametro en otra funcion. suena a global
    i = 0
    evaluated = False

    timesRepeated = letters.count(analizedLetter)
    if timesRepeated == 1:
        return evaluated 

    for letter in letters:
        if letter == analizedLetter and values[position] < values[i]:
            remainingWords = ''
            for word in wordsInFile:
                remainingWords += get_words_with_letter_in_position(word, letter, position)
            # se puede afinar mas:
            # si el valor inferior es 0 y el superior es 1, elimina todas las palabras con esa letra en esa posicion
            # si el valor es 0 y el superior es 2, elimina todas las palabras con esa letra en todas las posiciones menos en la de valor 2
            # si el valor es 1 y el superior 2, elimina las palabras que no contengan como minimo 2 veces ese valor
            writeWordsInFile(file, remainingWords)
            evaluated = True
        i += 1

    return evaluated

def get_words_with_letter_in_position(word, letter, position):
    return word if word[position] != letter else ''

def get_word_with_letter(word, letter):
    return word if letter not in word else ''

def get_word_without_letter_and_with_letter_in_position(word, letter, position):
    return word if (letter in word) and (word[position] != letter) else ''

def get_word_without_letter_in_that_position(word, letter, position):
    return word if word[position] == letter else ''

def createFile():
    filename = generateFileName()

    from os.path import exists
    if not exists(filename):
        populateFile(filename)
    return filename

def generateFileName():
    from datetime import datetime
    date = datetime.today().strftime('%Y-%m-%d')
    return date + '.txt'

def getWordsInFile(file):
    with open(file, 'r') as file:
        return file.readlines()

def writeWordsInFile(file, remainingWords):
    with open(file, 'w') as file:
        file.write(remainingWords)

def printNumberOfWords(file):
    words = getWordsInFile(file)
    numberOfWords = len(words)
    print(numberOfWords)

def populateFile(file):
    with open('five_char_words.txt', 'r') as fullWordsList:
        words = ''
        for word in fullWordsList:
            words += word
        writeWordsInFile(file, words)

deleteWords(wordleWord)
