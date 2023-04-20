from Dictionary import Dictionary
from userInterface import getMatches
WORD_LENGTH = 5
DICTIONARY_FILE = 'es.txt'

myDict = Dictionary(DICTIONARY_FILE, WORD_LENGTH)
attempts = 0

# loop game
while len(myDict.words) != 1 and attempts!= 5:
    print(f'remaining possible words: {len(myDict.words)}')
    print(myDict.words)
    matches = getMatches()
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
