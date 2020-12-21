# -*- coding: utf-8 -*-
"""10.1

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1amm0kK9H0ZHs_1S-nySfKWrfllRtyUkj
"""

import doctest

LETTER_TO_MORSE = {
    'A': '.-', 'B': '-...', 'C': '-.-.',
    'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..',
    'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-',
    'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', '1': '.----',
    '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...',
    '8': '---..', '9': '----.', '0': '-----',
    ', ': '--..--', '.': '.-.-.-', '?': '..--..',
    '/': '-..-.', '-': '-....-', '(': '-.--.', ')': '-.--.-',
    ' ': ' '
}


def encode(message):
    """
    Кодирует строку в соответсвии с таблицей азбуки Морзе
    >>> encode('B'*30) # doctest: +ELLIPSIS
    '-... ... -...'
    >>> encode('JK')
    '.- ...-'
    >>> encode('AAAA OP')
    '.-.-.-.- 
    .--.'
    >>> encode('SOS')
    '... --- ...'
    >>> encode(76)
    Traceback (most recent call last):
    TypeError: 'int' object is not iterable
    >>> encode('Hello World!')
    Traceback (most recent call last):
    KeyError: 'e'
    """
    encoded_signs = [
        LETTER_TO_MORSE[letter] for letter in message
    ]

    return ' '.join(encoded_signs)


if __name__ == "__main__":
    doctest.testmod()