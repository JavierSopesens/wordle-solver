from Dictionary import Dictionary
from userInterface import getMatches

WORD_LENGTH = 5
DICTIONARY_FILE = 'es.txt'

myDict = Dictionary(DICTIONARY_FILE, WORD_LENGTH)
attempts = 0

def handleRepeated(matches: list) -> list:
    sorted_matches = sortMatchesAlphabetically(matches)
    return controlRepeatedMatches(sorted_matches, matches)

def sortMatchesAlphabetically(matches: list) ->list:
    return sorted(matches, key = lambda x: ord(x[0]))

# magic numbers
def controlRepeatedMatches(sorted_matches:list, original_matches:list)->list:
    previous = sorted_matches[0]
    for current in sorted_matches[1:]:
        if current[0] == previous[0]:
            if current[1] == 0 and previous[1] == 0:
                original_matches[original_matches.index(previous)][1] = -1
            if current[1] == 0 and previous[1] != 0:
                original_matches[original_matches.index(current)][1] = -1
            if current[1] != 0 and previous[1] == 0:
                original_matches[original_matches.index(previous)][1] = -1
        previous = current
    return original_matches

def main():
    while len(myDict.words) != 1 and attempts != 5:
        print(f'remaining possible words: {len(myDict.words)}')
        print(myDict.words)
        matches = getMatches()

        matches = (matches)
        for index, match in enumerate(matches):
            myDict.reduceList(match[0], match[1], index)
        # mientras no esté hecho el modulo de sugerencia, hacer un print de las words
        # TODO suggestions module
        # testeo de funciones de userInterface y de nuevas funciones de la clase dictionary
        # control de errores si la lista esta vacia
        attempts += 1
        
if 'name' == __name__:
    main()