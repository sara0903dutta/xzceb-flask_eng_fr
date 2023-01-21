import unittest
from translator import english_to_french, french_to_english


class TestMachineTranslation(unittest.TestCase):
    def test_null_english_to_french(self):
        """Test for null input for english_to_french."""
        return self.assertRaises(ValueError, english_to_french, None)

    def test_null_french_to_english(self):
        """Test for null input for french_to_english."""
        return self.assertRaises(ValueError, french_to_english, None)

    def test_english_to_french(self):
        """Test for the translation of 'Hello'."""
        return self.assertEqual(english_to_french("Hello"), "Bonjour")

    def test_french_to_english(self):
        """Test for the translation of 'Bonjour'."""
        return self.assertEqual(french_to_english("Bonjour"), "Hello")


unittest.main()
