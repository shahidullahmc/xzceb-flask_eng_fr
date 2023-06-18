import unittest
from deep_translator import MyMemoryTranslator
from translator import english_to_french, french_to_english


class TestEnglishToFrench(unittest.TestCase):
    def test_hello_translation(self):
        english_text = "Hello"
        translated_text = english_to_french(english_text)
        self.assertEqual(translated_text, "Bonjour")

    def test_goodbye_translation(self):
        english_text = "Goodbye"
        translated_text = english_to_french(english_text)
        self.assertEqual(translated_text, "Au revoir")


class TestFrenchToEnglish(unittest.TestCase):
    def test_bonjour_translation(self):
        french_text = "Bonjour"
        translated_text = french_to_english(french_text)
        self.assertEqual(translated_text, "Hello")

    def test_au_revoir_translation(self):
        french_text = "Au revoir"
        translated_text = french_to_english(french_text)
        self.assertEqual(translated_text, "Goodbye")


if __name__ == '__main__':
    unittest.main()
