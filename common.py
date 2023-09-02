import hashlib
from base64 import b64encode

# a = 0, b = 1, c = 2 ... z = 25
digits = {c: i for i, c in enumerate('abcdefghijklmnopqrstuvwxyz')}

# turns a word (base 26) to a number (base 10)
def parse_number(number):
    assert number.isalpha()
    
    return sum(digits[digit] * (26 ** i)
               for i, digit in enumerate(reversed(number.lower())))

# sha1 hashes a string and returns the hash in base 64
def sha1_b64(text):
    return b64encode(hashlib.sha1(text.encode()).digest()).decode()
