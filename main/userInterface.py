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
    # this value wont be a list of dict cause keys cannot be repeated, and in that case, it would be
    # neither can be a set or a tuple cause we need to change values in specific cases
    # so it is a list of lists
    return list(map(list,zip(letters, values)))
