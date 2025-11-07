"""
Unit tests for the codec module.

This module contains comprehensive tests for the Codec and ROT13Codec classes.
"""

import unittest
from codec import Codec, ROT13Codec


class TestCodec(unittest.TestCase):
    """Test cases for the Codec class."""

    def test_encode_simple_string(self):
        """Test encoding a simple string."""
        data = "Hello, World!"
        encoded = Codec.encode(data)
        self.assertEqual(encoded, "SGVsbG8sIFdvcmxkIQ==")

    def test_decode_simple_string(self):
        """Test decoding a base64 string."""
        encoded_data = "SGVsbG8sIFdvcmxkIQ=="
        decoded = Codec.decode(encoded_data)
        self.assertEqual(decoded, "Hello, World!")

    def test_encode_decode_roundtrip(self):
        """Test that encoding and then decoding returns the original string."""
        original = "The quick brown fox jumps over the lazy dog"
        encoded = Codec.encode(original)
        decoded = Codec.decode(encoded)
        self.assertEqual(decoded, original)

    def test_encode_unicode(self):
        """Test encoding unicode characters."""
        data = "코덱스 테스트"
        encoded = Codec.encode(data)
        decoded = Codec.decode(encoded)
        self.assertEqual(decoded, data)

    def test_encode_empty_string_raises_error(self):
        """Test that encoding an empty string raises ValueError."""
        with self.assertRaises(ValueError):
            Codec.encode("")

    def test_decode_empty_string_raises_error(self):
        """Test that decoding an empty string raises ValueError."""
        with self.assertRaises(ValueError):
            Codec.decode("")

    def test_decode_invalid_base64_raises_error(self):
        """Test that decoding invalid base64 raises ValueError."""
        with self.assertRaises(ValueError):
            Codec.decode("This is not base64!")


class TestROT13Codec(unittest.TestCase):
    """Test cases for the ROT13Codec class."""

    def test_encode_simple_string(self):
        """Test encoding a simple string with ROT13."""
        data = "Hello, World!"
        encoded = ROT13Codec.encode(data)
        self.assertEqual(encoded, "Uryyb, Jbeyq!")

    def test_decode_simple_string(self):
        """Test decoding a ROT13 string."""
        encoded_data = "Uryyb, Jbeyq!"
        decoded = ROT13Codec.decode(encoded_data)
        self.assertEqual(decoded, "Hello, World!")

    def test_encode_decode_roundtrip(self):
        """Test that encoding and then decoding returns the original string."""
        original = "The quick brown fox jumps over the lazy dog"
        encoded = ROT13Codec.encode(original)
        decoded = ROT13Codec.decode(encoded)
        self.assertEqual(decoded, original)

    def test_encode_preserves_non_alpha(self):
        """Test that non-alphabetic characters are preserved."""
        data = "Hello123!@#"
        encoded = ROT13Codec.encode(data)
        self.assertEqual(encoded, "Uryyb123!@#")

    def test_encode_lowercase(self):
        """Test encoding lowercase letters."""
        data = "abcdefghijklmnopqrstuvwxyz"
        encoded = ROT13Codec.encode(data)
        self.assertEqual(encoded, "nopqrstuvwxyzabcdefghijklm")

    def test_encode_uppercase(self):
        """Test encoding uppercase letters."""
        data = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        encoded = ROT13Codec.encode(data)
        self.assertEqual(encoded, "NOPQRSTUVWXYZABCDEFGHIJKLM")

    def test_encode_empty_string_raises_error(self):
        """Test that encoding an empty string raises ValueError."""
        with self.assertRaises(ValueError):
            ROT13Codec.encode("")

    def test_decode_empty_string_raises_error(self):
        """Test that decoding an empty string raises ValueError."""
        with self.assertRaises(ValueError):
            ROT13Codec.decode("")


if __name__ == '__main__':
    unittest.main()
