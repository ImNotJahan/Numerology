from hashlib import sha1
from base64 import b64encode
from random import getrandbits

# a = 0, b = 1, c = 2 ... z = 25
digits = {c: i for i, c in enumerate('abcdefghijklmnopqrstuvwxyz')}
digits_inverse = {y: x for x, y in digits.items()}

# turns a word (base 26) to a number (base 10)
def parse_number(number):
    assert number.isalpha()
    
    return sum(digits[digit] * (26 ** i)
        for i, digit in enumerate(reversed(number.lower())))

# turns a number (base 10) into a word (base 26)
def parse_string(number):
    string = ""
    
    while(number > 0):
        remainder = number % 26
        string = digits_inverse[remainder] + string
        number = number // 26
 
    return string

# sha1 hashes a string and returns the hash in base 64
def sha1_b64(text):
    return b64encode(sha1(text.encode()).digest()).decode()

def rand_bool():
    return bool(getrandbits(1))
