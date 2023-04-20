from Dictionary import Dictionary
from userInterface import getMatches
from time import time
WORD_LENGTH = 5
DICTIONARY_FILE = 'es.txt'

myDict = Dictionary(DICTIONARY_FILE, WORD_LENGTH)
attempts = 0

def controlDuplicated(matches:list)->list:
    #if the word passed contain a letter repeated, it causes inconsistences addresses in this function.
    #if one letter is 1 or 2 and the other is 0, delete that letter to aboid malfuntions on above.
    
    letters = [letter for letter, value in matches]
    if len(letters) != len(set(letters)): #any letter is repeated
        #check if any value is 2 or 1 and another, 0
        ...

    return matches




# loop game
while len(myDict.words) != 1 and attempts!= 5:
    print(f'remaining possible words: {len(myDict.words)}')
    print(myDict.words)
    matches = getMatches()

    #si en la lista hay dos letras iguales y una es un 0, no la pases
    controlDuplicated(matches)

    for index, match in enumerate(matches):
        myDict.reduceList(match[0], int(match[1]), index)
    # mientras no esté hecho el modulo de sugerencia, hacer un print de las words
    # TODO suggestions module
    # TODO analisis repeated letters. si la palabra a buscar es audio y uso avala,
    # recibire un valor de 20000. lo cual borrara todos los elementos de la lista
    #   pero no dejara de funcionar
    # testeo de funciones de userInterface y de nuevas funciones de la clase dictionary
    # control de errores si la lista esta vacia
    attempts += 1
