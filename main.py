from config import *
from classes import File, Dictionary, Suggester
from helper.userInputs import getMatches
from helper.duplicateHandler import handleRepeated

def main() -> None:
    fileDict = File(DICTIONARY_FILE)
    words = fileDict.getContentByLength(WORD_LENGTH)
    myDict = Dictionary(words)
    attempts = 0

    while len(myDict.words) != 1 and attempts != MAX_ATTEMPTS:
        print(f'remaining possible words: {len(myDict.words)}')

        matches = getMatches()
        matches = handleRepeated(matches)

        for index, match in enumerate(matches):
            myDict.reduceList(letter_status=match.status, letter_char=match.letter, position=index)

        suggester = Suggester(myDict)
        print(f"suggested word to use: {suggester.recommendBestOption()}")

        attempts += 1


if __name__ == "__main__":
    main()
