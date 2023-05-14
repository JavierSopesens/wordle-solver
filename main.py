from config import FILE_PATH, WORD_LENGTH, MAX_ATTEMPTS
from classes import File, Glossary, Suggester
from helper import userInterface
from helper import duplicateHandler

def main() -> None:
    fileGlossary = File(FILE_PATH)
    words = fileGlossary.getContentByLength(WORD_LENGTH)
    myGlossary = Glossary(words)
    attempts = 0

    while len(myGlossary.words) != 1 and attempts != MAX_ATTEMPTS:
        print(f'remaining possible words: {len(myGlossary.words)}')

        userMatches = userInterface.getMatches()
        cleanMatches = duplicateHandler.handleRepeated(userMatches)

        for index, match in enumerate(cleanMatches):
            myGlossary.reduceList(letter_status=match.status, letter_char=match.letter, position=index)

        suggester = Suggester(myGlossary.words)
        print(f"suggested word to use: {suggester.recommendBestOption()}")

        attempts += 1


if __name__ == "__main__":
    main()
