from generate_trim_dict import getAllWords
import unittest

class TestReadDictionary(unittest.TestCase):
    def test_getAllWords(self):
        # normal flow
        words = getAllWords()
        self.assertTrue(type(words) == list)
        self.assertTrue(len(words) != 0)
        # file does not exist
        self.assertRaises(ValueError, getAllWords,'random.txt')

if __name__ == '__main__':
    unittest.main()