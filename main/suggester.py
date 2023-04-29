# # asignale una puntuación a una palabra dependiendo de las veces que aparezcan sus letras
# dictionary = {}
# for word in words:
#     word = word.rstrip()
#     value = 0
#     for char in word:
#         value += letters.get(char)
#     dictionary[word] = []
#     dictionary[word].append(value)

# sortedDictionary = {}
# for w in sorted(dictionary, key=dictionary.get, reverse=True)[:10]:
#     print(w, dictionary[w])
# # poner como primer opcion aquellas palabras que no tengan dos letras


class Suggester:
    def __init__(self):
        self.timesLetterRepeated = {}

    def countTimesEveryLetterIsRepeated(self, dictionary):
        for word in dictionary.words:
            for char in word:
                if char not in self.timesLetterRepeated:
                    self.timesLetterRepeated[char] = 1
                else:
                    self.timesLetterRepeated[char] += 1

    def sumWordValues():
        pass