# length of the word to search
WORD_LENGTH = 5

# language to play wordle
# POSSIBLES LANGUAGES ARE:
#   english -> eng
#   spanish -> es
#   if you have another dictionary, you can use that one inserting the file in the "glossary" folder
LANGUAGE = 'es'
DICTIONARY_FILE = LANGUAGE + '.txt'

# possible status of values associated to the chosen letters in every word
# DO NOT CHANGE THESE VALUES
TO_AVOID = -1 # only used in control of duplicated matches. final user do not uses it.
NOT_IN_THE_WORD = 0
IN_WORD_BUT_BAD_POSITION = 1
IN_WORD_AND_IN_PLACE = 2
