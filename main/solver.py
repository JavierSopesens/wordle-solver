from Dictionary import Dictionary
from File import File
from userInterface import getMatches
from Match import Match
from config import *

def handleRepeated(matches: list[Match]) -> list[Match]:
    sorted_matches = sortMatchesAlphabetically(matches)
    return controlRepeatedMatches(sorted_matches, matches)

def sortMatchesAlphabetically(matches: list[Match]) ->list[Match]:
    return sorted(matches, key = lambda i: i.letter)

# its possible to clearify parameters?
#o deberiamos crear una clase especial 3, (mas de 1 y en otro sitio)

# si vamos a poner todos los casos posibles, seria recomendable per cuando usar switch cases en python
def controlRepeatedMatches(sorted_matches:list[Match], original_matches:list[Match])->list[Match]:
    previous = sorted_matches[0]
    for current in sorted_matches[1:]:
        if current.letter == previous.letter:
            if current.status is NOT_IN_THE_WORD and previous.status is NOT_IN_THE_WORD:
                original_matches[original_matches.index(previous)].status = TO_AVOID
            if current.status is NOT_IN_THE_WORD and previous.status is not NOT_IN_THE_WORD:
                original_matches[original_matches.index(current)].status = TO_AVOID
            if current.status is not NOT_IN_THE_WORD and previous.status is NOT_IN_THE_WORD:
                original_matches[original_matches.index(previous)].status = TO_AVOID
        previous = current
    return original_matches


fileDict = File(DICTIONARY_FILE)
myDict = Dictionary(fileDict, WORD_LENGTH)
attempts = 0
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
    # docstrings
    # readme file
    attempts += 1


    # crear funcion main