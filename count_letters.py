with open('Dictionary/trimedDictionary.txt', 'r') as file:
    words = file.readlines()

# por cada letra, la introduce en el diccionario letters y cada vez que aparezca, le suma 1
letters = {}
for word in words:
    word = word.rstrip()
    for char in word:
        if char not in letters:
            letters[char] = 1
        else:
            letters[char] +=1 

            
# asignale una puntuación a una palabra dependiendo de las veces que aparezcan sus letras
dictionary = {} 
for word in words:
    word = word.rstrip()
    value = 0
    for char in word:
        value += letters.get(char)
    dictionary[word] = []
    dictionary[word].append(value)

sortedDictionary = {}
for w in sorted(dictionary, key=dictionary.get, reverse=True)[:10]:
    print(w, dictionary[w])
# poner como primer opcion aquellas palabras que no tengan dos letras

