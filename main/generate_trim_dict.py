def getAllWords(file: str = 'es.txt') -> list: 
    # input is str
    if type(file) != str:
        raise TypeError('file have to be string format')

    # file exists
    from pathlib import Path
    my_file = Path('Dictionary\\'+file)
    if not my_file.exists():
        raise ValueError('file does not exist')

    with open('Dictionary\\' + file, encoding='utf-8') as file:
        words = [line.rstrip() for line in file]
    return words


def trimWordsList(words: list[str], wordSize: int = 5) -> list:
    # if not all([words for word in words if type(word) == str]):
    if not isinstance(words,list):
        raise TypeError('format error: words')
    if not type(wordSize) == int:
        raise TypeError('format error: wordSize')
    if wordSize < 0:
        raise ValueError('word size cannot be negative')
        
    trimedList = [word for word in words if len(word) == wordSize]
    return trimedList


def writeTrimedList(words: list):
    f = open("Dictionary/trimedDictionary.txt", "w+")
    for word in words:
        f.write(word+'\n')


fullWordList = getAllWords()
trimedList = trimWordsList(fullWordList)
writeTrimedList(trimedList)
