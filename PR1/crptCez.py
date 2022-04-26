import math
from string import ascii_lowercase
from collections import Counter


ALPHABET = ascii_lowercase
ALPHABET_SIZE = len(ALPHABET)
LETTER_FREQUENCY = {'e': 12.7, 't': 9.06, 'a': 8.17, 'o': 7.51, 'i': 6.97, 'n': 6.75, 's': 6.33, 'h': 6.09,
                    'r': 5.99, 'd': 4.25, 'l': 4.03, 'c': 2.78, 'u': 2.76, 'm': 2.41, 'w': 2.36, 'f': 2.23,
                    'g': 2.02, 'y': 1.97, 'p': 1.93, 'b': 1.29, 'v': 0.98, 'k': 0.77, 'j': 0.15, 'x': 0.15,
                    'q': 0.10, 'z': 0.07}

GRAPH_STYLE = 'fivethirtyeight'
LETTERS_X = list(ascii_lowercase)


def cipher(text: str, key: int, decrypt: bool) -> str:
    output = ''
    text = text.lower()
    for char in text:
        # If the character is not in the english alphabet don't change it.
        if char not in ALPHABET:
            output += char
            continue

        index = ALPHABET.index(char.lower())

        if decrypt:
            new_char = ALPHABET[(index - key) % ALPHABET_SIZE]
        else:
            new_char = ALPHABET[(index + key) % ALPHABET_SIZE]

        # Setting the right case for the letter and adding it to the output
        output += new_char.upper() if char.isupper() else new_char
    return output


def difference(text: str) -> float:
    counter = Counter(text)
    return sum([abs(counter.get(letter, 0) * 100 / len(text) - LETTER_FREQUENCY[letter]) for letter in
                ALPHABET]) / ALPHABET_SIZE


def break_cipher(cipher_text: str) -> int:
    lowest_difference = math.inf
    encryption_key = 0

    for key in range(1, ALPHABET_SIZE):
        current_plain_text = cipher(cipher_text, key, True)
        current_difference = difference(current_plain_text)

        if current_difference < lowest_difference:
            lowest_difference = current_difference
            encryption_key = key

    return encryption_key

encrtext = cipher("MORE THEN ONE BOOK WE NEED TO READ", 12, False)
print('Possible encryption hack:')
print('Key pair A: {}'.format(break_cipher(encrtext)))
print('Decrypted message:')
print(cipher(encrtext, break_cipher(encrtext), True))