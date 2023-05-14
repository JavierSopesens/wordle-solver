from enum import Enum

# length of the word to search
WORD_LENGTH = 5

# max number of attempts to find the word
MAX_ATTEMPTS = 5

# language to play wordle
# POSSIBLES LANGUAGES ARE:
#   english -> eng
#   spanish -> es
#   if you have another dictionary, you can use that one inserting the file in the "glossary" folder
LANGUAGE = 'es'
GLOSSARY_FILE = LANGUAGE + '.txt'

# possible status of values associated to the chosen letters in every word
class MatchStatus(Enum):
    TO_AVOID = -1 # only used in control of duplicated matches. final user do not uses it.
    NOT_IN_WORD = 0
    IN_WORD_BUT_BAD_PLACE = 1
    IN_WORD_AND_IN_PLACE = 2
