with open('wordle/five_char_words.txt', encoding='utf-8') as file:
    lines = [line.rstrip() for line in file]
for word in lines:
    print(word)