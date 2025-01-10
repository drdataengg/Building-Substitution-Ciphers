# Ciphers Overview

A **cipher** is a method or algorithm used to encrypt and decrypt information to protect its confidentiality. It transforms plaintext (readable data) into ciphertext (unreadable format) using a specific set of rules or keys. Ciphers are foundational to cryptography and are used to ensure secure communication and data storage.

## Types of Ciphers

Ciphers can be broadly categorized into **classical ciphers** and **modern ciphers**:

### 1. Classical Ciphers

These are older methods used before the advent of computers. They are often used for educational purposes or in simple encryption scenarios.

#### a. Substitution Ciphers
- Replace each letter or symbol in the plaintext with another.
- Examples:
  - **Caesar Cipher**: Shifts each letter in the plaintext by a fixed number of positions.
  - **Monoalphabetic Cipher**: Each letter is replaced with a fixed corresponding letter.
  - **Vigenère Cipher**: Uses a keyword to determine the substitution for each letter.

#### b. Transposition Ciphers
- Rearrange the order of characters in the plaintext.
- Examples:
  - **Rail Fence Cipher**: Writes plaintext in a zigzag pattern across rows and reads it row by row.
  - **Columnar Transposition**: Rearranges columns of text based on a key.

#### c. Polygraphic Ciphers
- Encrypts multiple letters at a time.
- Example: **Playfair Cipher**: Encrypts digraphs (pairs of letters) using a 5x5 matrix.

### 2. Modern Ciphers

These ciphers rely on computational algorithms and are much more secure than classical ciphers.

#### a. Symmetric Key Ciphers
- The same key is used for both encryption and decryption.
- Examples:
  - **Block Ciphers**: Encrypt data in fixed-size blocks.
    - **AES (Advanced Encryption Standard)**: Highly secure, widely used.
    - **DES (Data Encryption Standard)**: Older, less secure.
  - **Stream Ciphers**: Encrypt data one bit or byte at a time.
    - **RC4**: A widely used stream cipher.

#### b. Asymmetric Key Ciphers
- Use a pair of keys: a public key for encryption and a private key for decryption.
- Examples:
  - **RSA**: Secure and widely used in digital signatures.
  - **ECC (Elliptic Curve Cryptography)**: Offers high security with smaller key sizes.

#### c. Hash Functions
- Convert data into a fixed-size hash value, not meant to be decrypted.
- Examples:
  - **SHA (Secure Hash Algorithm)**: Produces a unique hash for any input.
  - **MD5 (Message Digest 5)**: Older and less secure.

## Summary of Cipher Types

1. **Classical Ciphers**:
   - Substitution (e.g., Caesar, Vigenère)
   - Transposition (e.g., Rail Fence, Columnar)
   - Polygraphic (e.g., Playfair)
2. **Modern Ciphers**:
   - Symmetric (e.g., AES, DES)
   - Asymmetric (e.g., RSA, ECC)
   - Hash Functions (e.g., SHA, MD5)
