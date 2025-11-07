#!/usr/bin/env python3
"""
Example usage of the codec implementations.

This script demonstrates how to use the Codec and ROT13Codec classes.
"""

from codec import Codec, ROT13Codec


def main():
    """Main function demonstrating codec usage."""
    print("=" * 60)
    print("Codec Testing Examples")
    print("=" * 60)
    
    # Base64 Codec Examples
    print("\n1. Base64 Codec Examples")
    print("-" * 60)
    
    # Example 1: Simple English text
    text1 = "Hello, World!"
    encoded1 = Codec.encode(text1)
    decoded1 = Codec.decode(encoded1)
    print(f"Original: {text1}")
    print(f"Encoded:  {encoded1}")
    print(f"Decoded:  {decoded1}")
    print(f"Match:    {text1 == decoded1}")
    
    # Example 2: Korean text (코덱스 테스트)
    print("\n" + "-" * 60)
    text2 = "코덱스 테스트"
    encoded2 = Codec.encode(text2)
    decoded2 = Codec.decode(encoded2)
    print(f"Original: {text2}")
    print(f"Encoded:  {encoded2}")
    print(f"Decoded:  {decoded2}")
    print(f"Match:    {text2 == decoded2}")
    
    # ROT13 Codec Examples
    print("\n2. ROT13 Codec Examples")
    print("-" * 60)
    
    # Example 3: Simple English text
    text3 = "The quick brown fox jumps over the lazy dog"
    encoded3 = ROT13Codec.encode(text3)
    decoded3 = ROT13Codec.decode(encoded3)
    print(f"Original: {text3}")
    print(f"Encoded:  {encoded3}")
    print(f"Decoded:  {decoded3}")
    print(f"Match:    {text3 == decoded3}")
    
    # Example 4: Text with numbers and special characters
    print("\n" + "-" * 60)
    text4 = "Python 3.9+ supports Unicode! 🎉"
    encoded4 = ROT13Codec.encode(text4)
    decoded4 = ROT13Codec.decode(encoded4)
    print(f"Original: {text4}")
    print(f"Encoded:  {encoded4}")
    print(f"Decoded:  {decoded4}")
    print(f"Match:    {text4 == decoded4}")
    
    print("\n" + "=" * 60)
    print("All examples completed successfully!")
    print("=" * 60)


if __name__ == "__main__":
    main()
