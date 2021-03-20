import string
import typing as tp


def encrypt_caesar(plaintext: str, shift: int = 3) -> str:
    """
    Encrypts plaintext using a Caesar cipher.

    >>> encrypt_caesar("PYTHON")
    'SBWKRQ'
    >>> encrypt_caesar("python")
    'sbwkrq'
    >>> encrypt_caesar("Python3.6")
    'Sbwkrq3.6'
    >>> encrypt_caesar("")
    ''
    """
    ciphertext = ""
    # PUT YOUR CODE HERE
    for i in plaintext:
        if i == " ":
            ciphertext += " "
        else:
            f = string.ascii_lowercase.find(i)
            if f == -1:
                f = string.ascii_uppercase.find(i)
                if f == -1:
                    ciphertext += i
                else:
                    res = (f + shift) % len(string.ascii_uppercase)
                    ciphertext += string.ascii_uppercase[res]
            else:
                res = (f + shift) % len(string.ascii_lowercase)
                ciphertext += string.ascii_lowercase[res]
    return ciphertext


def decrypt_caesar(ciphertext: str, shift: int = 3) -> str:
    """
    Decrypts a ciphertext using a Caesar cipher.

    >>> decrypt_caesar("SBWKRQ")
    'PYTHON'
    >>> decrypt_caesar("sbwkrq")
    'python'
    >>> decrypt_caesar("Sbwkrq3.6")
    'Python3.6'
    >>> decrypt_caesar("")
    ''
    """
    plaintext = ""
    # PUT YOUR CODE HERE
    for i in ciphertext:
        if i == " ":
            plaintext += " "
        else:
            f = string.ascii_lowercase.find(i)
            if f == -1:
                f = string.ascii_uppercase.find(i)
                if f == -1:
                    plaintext += i
                else:
                    res = (f - shift) % len(string.ascii_uppercase)
                    plaintext += string.ascii_uppercase[res]
            else:
                res = (f - shift) % len(string.ascii_lowercase)
                plaintext += string.ascii_lowercase[res]
    return plaintext


def caesar_breaker_brute_force(ciphertext: str, dictionary: tp.Set[str]) -> int:
    """
    Brute force breaking a Caesar cipher.
    """
    best_shift = 0
    # PUT YOUR CODE HERE
    k = 0
    for shift in range(26):
        s = 0
        plaintext = decrypt_caesar(ciphertext, shift)
        mm = plaintext.split()
        for m in mm:
            if m in dictionary:
                s += 1
            if s > k:
                k = s
                best_shift = shift
    return best_shift
