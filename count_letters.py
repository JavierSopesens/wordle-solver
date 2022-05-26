# coge las palabras
f_lines = open('five_char_words.txt', 'r')
lines = f_lines.readlines()
f_lines.close()
# por cada letra, la introduce en el diccionario letters y cada vez que aparezca, le suma 1
letters = {}
for line in lines:
    line = line.rstrip()
    for char in line:
        if char not in letters:
            letters[char] = 1
        else:
            letters[char] +=1 

# asignale una puntuación a una palabra dependiendo de las veces que aparezcan sus letras
words = {}
for line in lines:
    line = line.rstrip()
    for char in line:
        words[line] = 0
        words[line] += letters[char]

#search the word with the higher value
# PROBLEMA!! Devuelve valores con letras repetidas. 
# Eliminar del diccionario aquellas que tengan letras repetidas!
#best_word = max(words, key=words.get)
#print(best_word)

