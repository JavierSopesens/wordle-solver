from Match import Match
WORD_LENGTH = 5

def getLetters()->list[str]:
    while True:
        letters = input('Write Word: ')
        if len(letters) != WORD_LENGTH:
            print('check the lenght of the word')
            continue
        if not letters.isalpha():
            print('word have to be composed only by letters')
            continue
        return letters

def getValues()->list[int]:
    while True:
        values = input('Write Values: ')
        if len(values) != WORD_LENGTH:
            print('check the lenght of the values')
            continue
        if not values.isnumeric():
            print('values have to be composed only by numbers')
            continue
        if any(char not in '012' for char in values):
            print('values can only be 0, 1 or 2')
            continue
        return list(map(int,values))

def getMatches() -> list[dict]:
    letters = getLetters()
    values = getValues()

    return [Match(letter, value) for letter, value in zip(letters, values)]