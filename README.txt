HOW IT WORKS
	This is a terminal-based Wordle solver.
	Executing main.py the program will ask for the word you used and the values and the color of every letter.
	Values have to be expressed as 0 (if not appears), 1 (if appears but it is in bad place) and 2 (if appears and it is in place).
	As example:
	letters -> audio
	values  -> 10012
	in this example 'a' and 'i' appears but they are in bad place, 'u' and 'd' not appears and 'o' appears and it is in the rigth place.
	After every itteration, it will appears a suggestion for the next word to use taking in count the remaining possible words and the frequency of every word in it.

	In the file config.py you can change certain variables as the language you are playing, the number of letters of the hidden word, etc.
	If you want to play in other languages, you only need to add a txt file with the words in that language in the glossary folder and change that global variable in the config.py file 

classes
	File -------------> Read the file with the words
	Glossary ---------> contains the words and the functions to reduce the list until find the hidden word
	Match ------------> dataclass with letter and value as parameter
	Suggester --------> used to suggest the better next word to use
	Word -------------> used to check if words contain certain letters, position of that letter and if has repeated letters

glossary -------------> contains documents to play in differents LANGUAGES
	es ---------------> glossary in spanish
	eng --------------> glossary in english

helper ---------------> contians packages with auxiliar functions
	duplicateHandler -> contains functions to handle the cases where letters are repeated in the same word used
	userInterface ----> contains functions to get the user inputs

tests ----------------> contain class tests
	test_file --------> tests class file
	test_glossary ----> test class glossary

config ---------------> contains necessary values to works. Values can be changed if necessary
main -----------------> contains the logic loop to play wordle


This project is not finished yet. It needs more testing among other things.

This is my first Python project :D 
enjoy it