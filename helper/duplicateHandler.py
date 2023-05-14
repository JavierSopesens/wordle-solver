from classes import Match
from config import MatchStatus

def handleRepeated(matches: list[Match]) -> list[Match]:
    sorted_matches = sortMatchesAlphabetically(matches)
    return controlRepeatedMatches(sorted_matches, matches)

def sortMatchesAlphabetically(matches: list[Match]) ->list[Match]:
    return sorted(matches, key = lambda i: i.letter)

def controlRepeatedMatches(sorted_matches:list[Match], original_matches:list[Match])->list[Match]:
    previous = sorted_matches[0]
    for current in sorted_matches[1:]:
        if current.letter == previous.letter:
            if current.status is MatchStatus.NOT_IN_WORD and previous.status is MatchStatus.NOT_IN_WORD:
                original_matches[original_matches.index(previous)].status = MatchStatus.TO_AVOID
            if current.status is MatchStatus.NOT_IN_WORD and previous.status is not MatchStatus.NOT_IN_WORD:
                original_matches[original_matches.index(current)].status = MatchStatus.TO_AVOID
            if current.status is not MatchStatus.NOT_IN_WORD and previous.status is MatchStatus.NOT_IN_WORD:
                original_matches[original_matches.index(previous)].status = MatchStatus.TO_AVOID
        previous = current
    return original_matches