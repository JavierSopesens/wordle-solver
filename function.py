word = [['a', 'u', 'd', 'i', 'o'], [2, 0, 2, 0, 1]]

LETTER_NOT_EXIST = 0
LETTER_EXIST_IN_OTHER_POSITION = 1
LETTER_IN_PLACE = 2

def reduce_list(word):
    letters = word[0]
    values = word[1]
    file = getFilename()
    count = 0

    printNumberOfWords(file)
    for letter in letters:
        lines = getWordsInFile(file)
        skip = evaluate_repetition(lines, file, count, letter, letters, values)
        if not skip:
            if values[count] == LETTER_NOT_EXIST:
                deleteWords(LETTER_NOT_EXIST, lines, file, letters[count], count)
            if values[count] == LETTER_EXIST_IN_OTHER_POSITION:
                deleteWords(LETTER_EXIST_IN_OTHER_POSITION, lines, file, letters[count], count)
            if values[count] == LETTER_IN_PLACE:
                deleteWords(LETTER_IN_PLACE, lines, file, letters[count], count)
        printNumberOfWords(file)
        count += 1
    # import os
    # os.remove(file)

def deleteWords(status, words, file, letter, position):
    remainingWords = ''
    with open(file, 'w') as file:
        for word in words:
            if status == LETTER_NOT_EXIST:
                remainingWords += get_word_with_letter(word, letter)
            if status == LETTER_EXIST_IN_OTHER_POSITION:
                remainingWords += get_word_without_letter_and_with_letter_in_position(
                    word, letter, position)
            if status == LETTER_IN_PLACE:
                remainingWords += get_word_without_letter_in_that_position(
                    word, letter, position)
        file.write(remainingWords)

def get_word_with_letter(word, letter):
    return word if letter not in word else ''

def get_word_without_letter_and_with_letter_in_position(word, letter, position):
    return word if (letter in word) and (word[position] != letter) else ''

def get_word_without_letter_in_that_position(word, letter, position):
    return word if word[position] == letter else ''


def evaluate_repetition(lines, file, position, analizedLetter, letters, values):
    # la variable file passa por aquí simplemente para ser un parametro en otra funcion. suena a global
    # el nombre de variable skip tampoco resulta del todo claro, dado que skip pasa a ser true precisamente cuando ejecuta una acción
    i = 0
    skip = False

    times = letters.count(analizedLetter)
    if times != 1:
        for letter in letters:
            if letter == analizedLetter:
                if values[position] < values[i]:
                    # se puede afinar mas:
                    # si el valor inferior es 0 y el superior es 1, elimina todas las palabras con esa letra en esa posicion
                    # si el valor es 0 y el superior es 2, elimina todas las palabras con esa letra en todas las posiciones menos en la de valor 2
                    # si el valor es 1 y el superior 2, elimina las palabras que no contengan como minimo 2 veces ese valor
                    delete_words_with_letter_in_position(lines, file, letter, position)
                    skip = True
            i += 1

    return skip

def getFilename():
    """
    If the file for today doesn't exist, create it and write the contents of the full word list to it
    :return: The name of the file that was created.
    """
    # MAYBE THE FULLWORDSLIST HAVE TO BE A GLOBAL?
    # ESTA FUNCIÓN HACE DOS COSAS:
    #   1. EVALUA SI EXISTE
    #   2. EN CASO DE NO EXISTIR, LO CREA Y LO RELLENA
    #       ERGO FUNCIÓN DIVISIBLE
    # fullWirdsList puede ser una global?
    # vols dir que no hay otra forma de evaluar si existe el fichero sin tener que importar paquetes?
    from datetime import datetime
    from os.path import exists
    date = datetime.today().strftime('%Y-%m-%d')
    filename = date + '.txt'

    if not exists(filename):
        with open("five_char_words.txt", "r+") as fullWordsList, open(filename, "w") as file:
            for word in fullWordsList:
                file.write(word)
    return filename

def getWordsInFile(file):
    with open(file, 'r') as file:
        return file.readlines()

def printNumberOfWords(file):
    words = getWordsInFile(file)
    numberOfWords = len(words)
    print(numberOfWords)

def delete_words_with_letter_in_position(words, file, letter, position):
    with open(file, 'w') as file:
        for word in words:
            if word[position] != letter:
                file.write(word)

reduce_list(word)
