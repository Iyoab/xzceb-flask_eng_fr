import unittest
from translator import english_to_french, french_to_english
class TestTranslator(unittest.TestCase):
    def test1_english_to_french(self):
        self.assertEqual(english_to_french("Yes"),"Oui")
    def test2_french_to_english(self):
        self.assertEqual(french_to_english("Oui"),"Yes")        
    def test_null_input_french_to_english(self):
        self.assertIsNone(None)
    def test_null_input_english_to_french(self):
        self.assertIsNone(None)
    def test1_french_to_english(self):
        self.assertEqual(french_to_english("Bonjour"),"Hello")
    def test2_english_to_french(self):
        self.assertEqual(english_to_french("Hello"),"Bonjour")