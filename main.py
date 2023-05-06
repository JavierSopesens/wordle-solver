from config import *
from classes import File, Dictionary, Suggester
from helper.userInputs import getMatches
from helper.duplicateHandler import handleRepeated

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