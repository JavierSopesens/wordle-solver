with open('wordle\es.txt', encoding='utf-8') as file:
    lines = [line.rstrip() for line in file]
    f= open("wordle/five_char_words.txt","w+")
    
# copy only words with 5 letters
for word in lines:
    if len(word) == 5:
        f.write(word +"\n")