from config import *
from classes import Match, File, Dictionary, Suggester
from classes.userInterface import getMatches


def handleRepeated(matches: list[Match]) -> list[Match]:
    sorted_matches = sortMatchesAlphabetically(matches)
    return controlRepeatedMatches(sorted_matches, matches)

def sortMatchesAlphabetically(matches: list[Match]) ->list[Match]:
    return sorted(matches, key = lambda i: i.letter)

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

def main() -> None:
    fileDict = File(DICTIONARY_FILE)
    myDict = Dictionary(fileDict, WORD_LENGTH)
    attempts = 0
    while len(myDict.words) != 1 and attempts != 5:
        print(f'remaining possible words: {len(myDict.words)}')

        matches = getMatches()
        matches = handleRepeated(matches)
        
        for index, match in enumerate(matches):
            myDict.reduceList(match, index)

        suggester = Suggester(myDict)
        print(suggester.recommendBestOption())
        
        attempts += 1

if __name__ ==  "__main__":
    main()