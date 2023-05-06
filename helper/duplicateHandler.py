from classes import Match
from config import NOT_IN_THE_WORD, TO_AVOID

def handleRepeated(matches: list[Match]) -> list[Match]:
    sorted_matches = sortMatchesAlphabetically(matches)
    return controlRepeatedMatches(sorted_matches, matches)

def sortMatchesAlphabetically(matches: list[Match]) ->list[Match]:
    return sorted(matches, key = lambda i: i.letter)

def controlRepeatedMatches(sorted_matches:list[Match], original_matches:list[Match])->list[Match]:
    previous = sorted_matches[0]
    for current in sorted_matches[1:]:
        if current.letter == previous.letter:
            if current.status is NOT_IN_THE_WORD and previous.status is NOT_IN_THE_WORD:
                original_matches[original_matches.index(previous)].status = TO_AVOID
            if current.status is NOT_IN_THE_WORD and previous.status is not NOT_IN_THE_WORD:
                original_matches[original_matches.index(current)].status = TO_AVOID
            if current.status is not NOT_IN_THE_WORD and previous.status is NOT_IN_THE_WORD:
                original_matches[original_matches.index(previous)].status = TO_AVOID
        previous = current
    return original_matches