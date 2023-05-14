from config import DICTIONARY_FILE, WORD_LENGTH, MAX_ATTEMPTS
from classes import File, Dictionary, Suggester
from helper import userInterface
from helper import duplicateHandler

def main() -> None:
    fileDict = File(DICTIONARY_FILE)
    words = fileDict.getContentByLength(WORD_LENGTH)
    myDict = Dictionary(words)
    attempts = 0

    while len(myDict.words) != 1 and attempts != MAX_ATTEMPTS:
        print(f'remaining possible words: {len(myDict.words)}')

        userMatches = userInterface.getUserMatches()
        cleanMatches = duplicateHandler.handleRepeated(userMatches)

        for index, match in enumerate(cleanMatches):
            myDict.reduceList(letter_status=match.status, letter_char=match.letter, position=index)

        suggester = Suggester(myDict.words)
        print(f"suggested word to use: {suggester.recommendBestOption()}")

        attempts += 1


if __name__ == "__main__":
    main()
