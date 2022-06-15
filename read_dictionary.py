def getAllWords(file: str = 'es.txt') -> list:
    with open('Dictionary\\' + file, encoding='utf-8') as file:
        words = [line.rstrip() for line in file]
    return words


def trimWordsList(words: list, wordSize: int = 5) -> list:
    trimedList = [word+'\n' for word in words if len(word) == wordSize]
    return trimedList


def writeTrimedList(words: list):
    f = open("Dictionary/trimedDictionary.txt", "w+")
    for word in words:
        f.write(word)


fullWordList = getAllWords()
trimedList = trimWordsList(fullWordList)
writeTrimedList(trimedList)
