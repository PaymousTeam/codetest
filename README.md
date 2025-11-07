# codetest

A simple codec implementation for testing encoding and decoding functionality.

## Overview

This repository contains two codec implementations:
1. **Codec**: A Base64 encoder/decoder
2. **ROT13Codec**: A ROT13 cipher encoder/decoder

## Features

- Base64 encoding and decoding
- ROT13 cipher encoding and decoding
- Unicode support
- Comprehensive error handling
- Full test coverage

## Usage

### Base64 Codec

```python
from codec import Codec

# Encoding
original = "Hello, World!"
encoded = Codec.encode(original)
print(f"Encoded: {encoded}")  # Output: SGVsbG8sIFdvcmxkIQ==

# Decoding
decoded = Codec.decode(encoded)
print(f"Decoded: {decoded}")  # Output: Hello, World!

# Unicode support
korean = "코덱스 테스트"
encoded_kr = Codec.encode(korean)
decoded_kr = Codec.decode(encoded_kr)
print(f"Decoded Korean: {decoded_kr}")  # Output: 코덱스 테스트
```

### ROT13 Codec

```python
from codec import ROT13Codec

# Encoding
original = "Hello, World!"
encoded = ROT13Codec.encode(original)
print(f"Encoded: {encoded}")  # Output: Uryyb, Jbeyq!

# Decoding (ROT13 is its own inverse)
decoded = ROT13Codec.decode(encoded)
print(f"Decoded: {decoded}")  # Output: Hello, World!
```

## Running Tests

Run the test suite using Python's unittest:

```bash
python3 -m unittest test_codec.py -v
```

## Test Coverage

The test suite includes:
- Basic encoding and decoding tests
- Round-trip encoding/decoding tests
- Unicode character support tests
- Edge case handling (empty strings, invalid input)
- Preservation of non-alphabetic characters (ROT13)

## Requirements

- Python 3.6 or higher
- No external dependencies (uses only standard library)

## License

This is a test repository for demonstration purposes.