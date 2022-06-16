import read_dictionary
import unittest

class TestReadDictionary(unittest.TestCase):
    def test_getAllWords(self):
        # normal flow
        words = read_dictionary.getAllWords()
        self.assertTrue(type(words) == list)
        self.assertTrue(len(words) != 0)
        # file does not exist
        self.assertRaises(ValueError, read_dictionary.getAllWords,'random.txt')

if __name__ == '__main__':
    unittest.main()