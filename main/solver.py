from Dictionary import Dictionary

WORD_LENGTH = 5
DICTIONARY_FILE = 'es.txt'

myDict = Dictionary(DICTIONARY_FILE, WORD_LENGTH)
attempts = 0

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

def getValues()->list[str]:
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
        return values

def getMatches() -> list[dict]:
    letters = getLetters()
    values = getValues()

    return dict(zip(letters, values))

# loop game
while len(myDict.words) != 1 and attempts!= 5:
    print(f'remaining possible words: {len(myDict.words)}')
    print(myDict.words)
    matches = getMatches()
    for index, (key, value) in enumerate(matches.items()):
        myDict.reduceList(key, int(value), index)
    # mientras no esté hecho el modulo de sugerencia, hacer un print de las words
    
    attempts += 1
