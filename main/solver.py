from Dictionary import Dictionary
from userInterface import getMatches
from Match import Match

WORD_LENGTH = 5
DICTIONARY_FILE = 'es.txt'

myDict = Dictionary(DICTIONARY_FILE, WORD_LENGTH)
attempts = 0

def handleRepeated(matches: list) -> list:
    sorted_matches = sortMatchesAlphabetically(matches)
    return controlRepeatedMatches(sorted_matches, matches)

def sortMatchesAlphabetically(matches: list) ->list:
    return sorted(matches, key = lambda i: i.letter)

# magic numbers
# its possible to clearify parameters?
# value change to status
def controlRepeatedMatches(sorted_matches:list, original_matches:list)->list:
    previous = sorted_matches[0]
    for current in sorted_matches[1:]:
        if current.letter == previous.letter:
            if current.value == 0 and previous.value == 0:
                original_matches[original_matches.index(previous)].value = -1
            if current.value == 0 and previous.value != 0:
                original_matches[original_matches.index(current)].value = -1
            if current.value != 0 and previous.value == 0:
                original_matches[original_matches.index(previous)].value = -1
        previous = current
    return original_matches

while len(myDict.words) != 1 and attempts != 5:
    print(f'remaining possible words: {len(myDict.words)}')
    print(myDict.words)
    matches = getMatches()

    matches = handleRepeated(matches)
    for index, match in enumerate(matches):
        myDict.reduceList(match, index)
    # mientras no esté hecho el modulo de sugerencia, hacer un print de las words
    # TODO suggestions module
    # testeo de funciones de userInterface y de nuevas funciones de la clase dictionary
    # control de errores si la lista esta vacia
    attempts += 1


    # crear funcion main
    # eliminar magic numbers
    # fichero config con las globales
    # a partir de la linea 19 de este documento 
    #   y en todo el doc Dictionary.py 
    #   no estan implementadas las clases match