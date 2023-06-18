"""
This module provides functions for translating text between English and French.
"""

from deep_translator import MyMemoryTranslator


def english_to_french(english_text):
    """
    Translates English text to French.
    """
    translated_text = MyMemoryTranslator(source='en', target='fr').translate(english_text)
    return translated_text


def french_to_english(french_text):
    """
    Translates French text to English.
    """
    translated_text = MyMemoryTranslator(source='fr', target='en').translate(french_text)
    return translated_text
    