from Dictionary import Dictionary
from userInterface import getMatches

WORD_LENGTH = 5
DICTIONARY_FILE = 'es.txt'

myDict = Dictionary(DICTIONARY_FILE, WORD_LENGTH)
attempts = 0

# editar esta funcion. varios codesmell
# magic numbers
# hace varias cosas en una misma funcion
# primero ordena, luego evalue repeticiones y luego cambia valores 
def controlDuplicated(matches: list) -> list:
    sorted_matches = sorted(matches, key=lambda x: ord(x[0]))
    anterior = sorted_matches[0]
    for elemento in sorted_matches[1:]:
        if elemento[0] == anterior[0]:
            if elemento[1] == 0 and anterior[1] == 0:
                matches[matches.index(anterior)][1] = 3
            if elemento[1] == 0 and anterior[1] != 0:
                matches[matches.index(elemento)][1] = 3
            if elemento[1] != 0 and anterior[1] == 0:
                matches[matches.index(anterior)][1] = 3
        anterior = elemento
    return matches


# loop game
while len(myDict.words) != 1 and attempts != 5:
    print(f'remaining possible words: {len(myDict.words)}')
    print(myDict.words)
    matches = getMatches()

    # si en la lista hay dos letras iguales y una es un 0, no la pases
    matches = controlDuplicated(matches)
    for index, match in enumerate(matches):
        myDict.reduceList(match[0], match[1], index)
    # mientras no esté hecho el modulo de sugerencia, hacer un print de las words
    # TODO suggestions module
    # testeo de funciones de userInterface y de nuevas funciones de la clase dictionary
    # control de errores si la lista esta vacia
    attempts += 1
