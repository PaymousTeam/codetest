"""
Simple Codec Implementation for Testing

This module provides basic encoding and decoding functionality
for demonstrating codec operations.
"""

import base64


class Codec:
    """
    A simple codec class that provides encoding and decoding functionality.
    """

    @staticmethod
    def encode(data: str) -> str:
        """
        Encode a string to base64.

        Args:
            data (str): The input string to encode

        Returns:
            str: The base64 encoded string

        Raises:
            ValueError: If input data is empty
        """
        if not data:
            raise ValueError("Input data cannot be empty")
        
        bytes_data = data.encode('utf-8')
        encoded_bytes = base64.b64encode(bytes_data)
        return encoded_bytes.decode('utf-8')

    @staticmethod
    def decode(encoded_data: str) -> str:
        """
        Decode a base64 encoded string.

        Args:
            encoded_data (str): The base64 encoded string to decode

        Returns:
            str: The decoded string

        Raises:
            ValueError: If input data is empty or invalid base64
        """
        if not encoded_data:
            raise ValueError("Input data cannot be empty")
        
        try:
            bytes_data = encoded_data.encode('utf-8')
            decoded_bytes = base64.b64decode(bytes_data)
            return decoded_bytes.decode('utf-8')
        except Exception as e:
            raise ValueError(f"Invalid base64 data: {e}")


class ROT13Codec:
    """
    A ROT13 codec implementation for simple character rotation.
    """

    @staticmethod
    def encode(data: str) -> str:
        """
        Encode a string using ROT13.

        Args:
            data (str): The input string to encode

        Returns:
            str: The ROT13 encoded string

        Raises:
            ValueError: If input data is empty
        """
        if not data:
            raise ValueError("Input data cannot be empty")
        
        result = []
        for char in data:
            if 'a' <= char <= 'z':
                result.append(chr((ord(char) - ord('a') + 13) % 26 + ord('a')))
            elif 'A' <= char <= 'Z':
                result.append(chr((ord(char) - ord('A') + 13) % 26 + ord('A')))
            else:
                result.append(char)
        return ''.join(result)

    @staticmethod
    def decode(encoded_data: str) -> str:
        """
        Decode a ROT13 encoded string.
        
        Note: ROT13 is its own inverse, so encoding and decoding are the same.

        Args:
            encoded_data (str): The ROT13 encoded string to decode

        Returns:
            str: The decoded string

        Raises:
            ValueError: If input data is empty
        """
        return ROT13Codec.encode(encoded_data)
