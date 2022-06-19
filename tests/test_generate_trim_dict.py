from main.generate_trim_dict import getAllWords, trimWordsList, writeTrimedList
import pytest

# getAllWords TESTS


def test_getAllWords_use_case_empty_arg() -> None:
    words = getAllWords()
    assert type(words) == list
    assert len(words) != 0


def test_getAllWords_use_case_rigth_fill_arg() -> None:
    words = getAllWords('es.txt')
    assert type(words) == list
    assert len(words) != 0


def test_getAllWords_edge_case_file_not_exist() -> None:
    with pytest.raises(ValueError):
        getAllWords('random.txt')


def test_getAllWords_edge_case_not_string() -> None:
    with pytest.raises(TypeError):
        getAllWords(0)


# trimWordsList TESTS
def test_trimWordsList_use_case_wo_wordSize() -> None:
    words: list[str] = ['test', 'testtest', 'test5']
    output = trimWordsList(words)
    assert output == ['test5']


def test_trimWordsList_use_case_with_wordSize() -> None:
    words: list[str] = ['test', 'testtest', 'test5']
    output = trimWordsList(words, 4)
    assert output == ['test']


def test_trimWordsList_edge_case_list_wo_5chars_words() -> None:
    words: list[str] = ['test', 'testtest', 'testtesttest']
    output = trimWordsList(words)
    assert output == []


def test_trimWordsList_edge_case_all_words_5chars() -> None:
    # list with all words with 5 chars
    words: list[str] = ['test0', 'test1', 'test2']
    output = trimWordsList(words)
    assert output == ['test0', 'test1', 'test2']


def test_trimWordsList_edge_case_words_type_int() -> None:
    # words arg of type int
    words = 12345
    with pytest.raises(TypeError):
        trimWordsList(words)


def test_trimWordsList_edge_case_words_type_str() -> None:
    # words arg of type str
    words = 'five'
    with pytest.raises(TypeError):
        trimWordsList(words)


def test_trimWordsList_edge_case_wordsSize_type_str() -> None:
    # wordsSize not int
    words = ['test0', 'test1', 'test2']
    wordsSize = 'five'
    with pytest.raises(TypeError):
        trimWordsList(words, wordsSize)


def test_trimWordsList_edge_case_not_args() -> None:
    # not passing arg
    with pytest.raises(TypeError):
        trimWordsList()


def test_trimWordsList_edge_case_empty_list() -> None:
    # empty list
    words: list[str] = []
    output = trimWordsList(words)
    assert output == []


def test_trimWordsList_edge_case_wordSize_0() -> None:
    # word size == 0
    words: list[str] = ['test0', 'test1', 'test2']
    output = trimWordsList(words, 0)
    assert output == []


def test_trimWordsList_edge_case_wordSize_5() -> None:
    # word size == 5
    words: list[str] = ['test0', 'test1', 'test2']
    output = trimWordsList(words, 5)
    assert output == ['test0', 'test1', 'test2']


def test_trimWordsList_edge_case_wordSize_100() -> None:
    # word size == 100
    words: list[str] = ['test0', 'test1', 'test2']
    output = trimWordsList(words, 100)
    assert output == []


def test_trimWordsList_edge_case_wordSize_minus1() -> None:
    # word size == -1
    words: list[str] = ['test0', 'test1', 'test2']
    with pytest.raises(ValueError):
        trimWordsList(words, -1)

# writeTrimList TESTS
# not passing arg
# empty list
# full list
