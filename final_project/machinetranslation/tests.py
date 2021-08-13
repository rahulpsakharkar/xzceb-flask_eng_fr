import unittest

from translator import english_too_french, french_to_english

class TestEnglishToFrench(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(english_too_french('Hello'), 'Bonjour')
        with self.assertRaises(Exception):  
            english_too_french()  # Null input

class TestFrenchToEnglish(unittest.TestCase): 
    def test2(self): 
        self.assertEqual(french_to_english('Bonjour'), 'Hello')
        with self.assertRaises(Exception):
            french_to_english()  # Null input

unittest.main()