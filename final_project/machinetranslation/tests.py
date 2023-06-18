import unittest
from deep_translator import MyMemoryTranslator
from translator import english_to_french, french_to_english


class TestEnglishToFrench(unittest.TestCase):
    def test_hello_translation(self):
        english_text = "Hello"
        translated_text = english_to_french(english_text)
        self.assertEqual(translated_text, "Pepitoooo")

    def test_translation_not_equal(self):
        english_text = "Hello"
        translated_text = english_to_french(english_text)
        self.assertNotEqual(translated_text, "Hello")


class TestFrenchToEnglish(unittest.TestCase):
    def test_bonjour_translation(self):
        french_text = "Bonjour"
        translated_text = french_to_english(french_text)
        self.assertEqual(translated_text, "Hello")

    def test_translation_not_equal(self):
        french_text = "Bonjour"
        translated_text = french_to_english(french_text)
        self.assertNotEqual(translated_text, "Bonjour")


if __name__ == '__main__':
    unittest.main()
