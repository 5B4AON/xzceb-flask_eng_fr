'''Unit Tests for translator module'''
import unittest
from translator import english_to_french, french_to_english

class TestEnglishToFrench(unittest.TestCase):
    '''Test Cases for English to French function'''

    def test_bad_input(self):
        '''Test various cases of bad input'''
        # Test for no argument
        self.assertRaises(TypeError, english_to_french)
        # Test for null argument
        self.assertRaises(ValueError, english_to_french, None)
        # Test for empty string argument
        self.assertRaises(ValueError, english_to_french, '')

    def test_translation_result(self):
        '''Test result for good input'''
        self.assertEqual(english_to_french('Hello')['translations'][0]['translation'],'Bonjour')

class TestFrenchToEnglish(unittest.TestCase):
    '''Test Cases for French to English function'''

    def test_bad_input(self):
        '''Test various cases of bad input'''
        # Test for no argument
        self.assertRaises(TypeError, french_to_english)
        # Test for null argument
        self.assertRaises(ValueError, french_to_english, None)
        # Test for empty string argument
        self.assertRaises(ValueError, french_to_english, '')

    def test_translation_result(self):
        '''Test result for good input'''
        self.assertEqual(french_to_english('Bonjour')['translations'][0]['translation'],'Hello')

if __name__ == '__main__':
    unittest.main()
