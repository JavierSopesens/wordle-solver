wordleWord = [['a', 'u', 'd', 'i', 'o'], [2, 0, 2, 0, 1]]

LETTER_NOT_EXIST = 0
LETTER_EXIST_IN_OTHER_POSITION = 1
LETTER_IN_PLACE = 2

def reduceListOfWords(wordleWord):
    letters = wordleWord[0]
    values = wordleWord[1]
    file = getFilename()
    count = 0

    printNumberOfWords(file)
    for letter in letters:
        WordsInFile = getWordsInFile(file)
        evaluated = evaluateRepeatedLetters(WordsInFile, file, count, letter, letters, values)
        if not evaluated:
            # values[count] no es autoexplicativo!
            deleteWords(values[count], WordsInFile, file, letter, count)
        printNumberOfWords(file)
        count += 1
    # import os
    # os.remove(file)

def deleteWords(status, WordsInFile, file, letter, position):
    remainingWords = ''
    for word in WordsInFile:
        if status == LETTER_NOT_EXIST:
            remainingWords += get_word_with_letter(word, letter)
        if status == LETTER_EXIST_IN_OTHER_POSITION:
            remainingWords += get_word_without_letter_and_with_letter_in_position(word, letter, position)
        if status == LETTER_IN_PLACE:
            remainingWords += get_word_without_letter_in_that_position(word, letter, position)
    writeWordsInFile(file, remainingWords)

def get_word_with_letter(word, letter):
    return word if letter not in word else ''

def get_word_without_letter_and_with_letter_in_position(word, letter, position):
    return word if (letter in word) and (word[position] != letter) else ''

def get_word_without_letter_in_that_position(word, letter, position):
    return word if word[position] == letter else ''

def evaluateRepeatedLetters(wordsInFile, file, position, analizedLetter, letters, values):
    # la variable file passa por aquí simplemente para ser un parametro en otra funcion. suena a global
    # el nombre de variable skip tampoco resulta del todo claro, dado que skip pasa a ser true precisamente cuando ejecuta una acción
    i = 0
    skip = False

    times = letters.count(analizedLetter)
    if times != 1:
        for letter in letters:
            if letter == analizedLetter and values[position] < values[i]:
                # se puede afinar mas:
                # si el valor inferior es 0 y el superior es 1, elimina todas las palabras con esa letra en esa posicion
                # si el valor es 0 y el superior es 2, elimina todas las palabras con esa letra en todas las posiciones menos en la de valor 2
                # si el valor es 1 y el superior 2, elimina las palabras que no contengan como minimo 2 veces ese valor
                delete_words_with_letter_in_position(wordsInFile , file, letter, position)
                skip = True
            i += 1

    return skip

def getFilename():
    from datetime import datetime
    from os.path import exists
    date = datetime.today().strftime('%Y-%m-%d')
    filename = date + '.txt'

    if not exists(filename):
        generateFile(filename)
    return filename

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

def generateFile(file):
    with open('five_char_words.txt', 'r') as fullWordsList:
        words = ''
        for word in fullWordsList:
            words += word
        writeWordsInFile(file, words)

def delete_words_with_letter_in_position(words, file, letter, position):
    remainingWords = ''
    for word in words:
        if word[position] != letter:
            remainingWords += word
    writeWordsInFile(file, remainingWords)

reduceListOfWords(wordleWord)
