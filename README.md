
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Ciphers Overview</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            margin: 20px;
        }
        h1, h2, h3 {
            color: #2c3e50;
        }
        ul {
            margin-left: 20px;
        }
        code {
            background-color: #f4f4f4;
            padding: 2px 4px;
            border-radius: 4px;
        }
    </style>
</head>
<body>
    <h1>Ciphers Overview</h1>
    <p>A <strong>cipher</strong> is a method or algorithm used to encrypt and decrypt information to protect its confidentiality. It transforms plaintext (readable data) into ciphertext (unreadable format) using a specific set of rules or keys. Ciphers are foundational to cryptography and are used to ensure secure communication and data storage.</p>

    <h2>Types of Ciphers</h2>
    <p>Ciphers can be broadly categorized into <strong>classical ciphers</strong> and <strong>modern ciphers</strong>:</p>

    <h3>1. Classical Ciphers</h3>
    <p>These are older methods used before the advent of computers. They are often used for educational purposes or in simple encryption scenarios.</p>

    <h4>a. Substitution Ciphers</h4>
    <ul>
        <li>Replace each letter or symbol in the plaintext with another.</li>
        <li>Examples:
            <ul>
                <li><strong>Caesar Cipher</strong>: Shifts each letter in the plaintext by a fixed number of positions.</li>
                <li><strong>Monoalphabetic Cipher</strong>: Each letter is replaced with a fixed corresponding letter.</li>
                <li><strong>Vigenère Cipher</strong>: Uses a keyword to determine the substitution for each letter.</li>
            </ul>
        </li>
    </ul>

    <h4>b. Transposition Ciphers</h4>
    <ul>
        <li>Rearrange the order of characters in the plaintext.</li>
        <li>Examples:
            <ul>
                <li><strong>Rail Fence Cipher</strong>: Writes plaintext in a zigzag pattern across rows and reads it row by row.</li>
                <li><strong>Columnar Transposition</strong>: Rearranges columns of text based on a key.</li>
            </ul>
        </li>
    </ul>

    <h4>c. Polygraphic Ciphers</h4>
    <ul>
        <li>Encrypts multiple letters at a time.</li>
        <li>Example: <strong>Playfair Cipher</strong>: Encrypts digraphs (pairs of letters) using a 5x5 matrix.</li>
    </ul>

    <h3>2. Modern Ciphers</h3>
    <p>These ciphers rely on computational algorithms and are much more secure than classical ciphers.</p>

    <h4>a. Symmetric Key Ciphers</h4>
    <ul>
        <li>The same key is used for both encryption and decryption.</li>
        <li>Examples:
            <ul>
                <li><strong>Block Ciphers</strong>: Encrypt data in fixed-size blocks.
                    <ul>
                        <li><strong>AES (Advanced Encryption Standard)</strong>: Highly secure, widely used.</li>
                        <li><strong>DES (Data Encryption Standard)</strong>: Older, less secure.</li>
                    </ul>
                </li>
                <li><strong>Stream Ciphers</strong>: Encrypt data one bit or byte at a time.
                    <ul>
                        <li><strong>RC4</strong>: A widely used stream cipher.</li>
                    </ul>
                </li>
            </ul>
        </li>
    </ul>

    <h4>b. Asymmetric Key Ciphers</h4>
    <ul>
        <li>Use a pair of keys: a public key for encryption and a private key for decryption.</li>
        <li>Examples:
            <ul>
                <li><strong>RSA</strong>: Secure and widely used in digital signatures.</li>
                <li><strong>ECC (Elliptic Curve Cryptography)</strong>: Offers high security with smaller key sizes.</li>
            </ul>
        </li>
    </ul>

    <h4>c. Hash Functions</h4>
    <ul>
        <li>Convert data into a fixed-size hash value, not meant to be decrypted.</li>
        <li>Examples:
            <ul>
                <li><strong>SHA (Secure Hash Algorithm)</strong>: Produces a unique hash for any input.</li>
                <li><strong>MD5 (Message Digest 5)</strong>: Older and less secure.</li>
            </ul>
        </li>
    </ul>

    <h2>Summary of Cipher Types</h2>
    <ul>
        <li><strong>Classical Ciphers</strong>:
            <ul>
                <li>Substitution (e.g., Caesar, Vigenère)</li>
                <li>Transposition (e.g., Rail Fence, Columnar)</li>
                <li>Polygraphic (e.g., Playfair)</li>
            </ul>
        </li>
        <li><strong>Modern Ciphers</strong>:
            <ul>
                <li>Symmetric (e.g., AES, DES)</li>
                <li>Asymmetric (e.g., RSA, ECC)</li>
                <li>Hash Functions (e.g., SHA, MD5)</li>
            </ul>
        </li>
    </ul>
</body>
</html>







https://www.freecodecamp.org/learn/scientific-computing-with-python/#learn-string-manipulation-by-building-a-cipher 
 
