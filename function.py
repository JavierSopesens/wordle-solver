word = [['a', 'u', 'd', 'i', 'o'], [1, 0, 0, 0, 0]]

LETTER_NOT_EXIST = 0
LETTER_EXIST_IN_OTHER_POSITION = 1
LETTER_IN_PLACE = 2

def reduce_list(word):
    file = getFilename()
    count = 0
    printNumberOfWords(file)
    #word[0] definitivamente tiene que ser un nombre propio
    for letter in word[0]:
        lines = getWordsInFile(file)
        skip = evaluate_repetition(lines, file, count, letter)
        if skip:
            #las dos siguientes lineas de codigo se encuentran tambien al finalizar esta funcion
            printNumberOfWords(file)
            count+=1
            continue
        if word[1][count] == LETTER_NOT_EXIST:
            delete_words_with_letter(lines, file, word[0][count])
        if word[1][count] == LETTER_EXIST_IN_OTHER_POSITION:
            delete_words_without_letter_and_with_letter_in_position(lines, file, word[0][count], count)
        if word[1][count] == LETTER_IN_PLACE:
            delete_words_without_letter_in_that_position(lines, file, word[0][count], count)
        printNumberOfWords(file)
        count += 1
    import os
    os.remove(file)


def evaluate_repetition(lines, file, position, letter):
    #ese global me suena super fishy
    #la variable file passa por aquí simplemente para ser un parametro en otra funcion. suena a global
    #el nombre de variable skip tampoco resulta del todo claro, dado que skip pasa a ser true precisamente cuando ejecuta una acción
    global word
    where = []
    i = 0
    skip = False

    for char in word[0]:
        if char == letter:
            where.append(i)
        i += 1
    times = word[0].count(letter)
    if times != 1:
        for value in where:
            if word[1][position] < word[1][value]:
                delete_words_with_letter_in_position(lines, file, letter, position)
                skip = True
    return skip

def getFilename():
    """
    If the file for today doesn't exist, create it and write the contents of the full word list to it
    :return: The name of the file that was created.
    """
    #MAYBE THE FULLWORDSLIST HAVE TO BE A GLOBAL?
    #ESTA FUNCIÓN HACE DOS COSAS: 
    #   1. EVALUA SI EXISTE
    #   2. EN CASO DE NO EXISTIR, LO CREA Y LO RELLENA
    #       ERGO FUNCIÓN DIVISIBLE
    #fullWirdsList puede ser una global?
    #vols dir que no hay otra forma de evaluar si existe el fichero sin tener que importar paquetes?
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
    # posible sintaxis alternativa para readlines?
    with open(file, 'r') as file:
        wordsInFile = file.readlines()
    return wordsInFile

def printNumberOfWords(file):
    words = getWordsInFile(file)
    numberOfWords = len(words)
    print(numberOfWords)

#en las funciones delete:
#podemos convertirlas en una primera funcion "delete" para luego dirigir el flujo de la operación ahi donde sea necesario?

#buscar un metodo para no tener que reescribir todo el documento una y otra vez, 
# sino ir quitando las palabras que no toquen, en lugar de escribir constantemente las que si tocan
def delete_words_with_letter(words, file, letter):
    with open(file, 'w') as file:
        for word in words:
            if letter not in word:
                file.write(word)

def delete_words_without_letter_and_with_letter_in_position(words, file, letter, position):
    with open(file, 'w') as file:
        for word in words:
            if (letter in word) and (word[position] != letter):
                file.write(word)

def delete_words_without_letter_in_that_position(words, file, letter, position):
    with open(file, 'w') as file:
        for word in words:
            if word[position] == letter:
                file.write(word)

def delete_words_with_letter_in_position(words, file, letter, position):
    with open(file, 'w') as file:
        for word in words:
            if word[position] != letter:
                file.write(word)

reduce_list(word)
