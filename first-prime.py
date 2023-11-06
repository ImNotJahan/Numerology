'''
Adds 1 to a number until it's prime (in base 26)
'''

from sympy.ntheory import isprime
from common import parse_number, parse_string

num = parse_number(input())

while(not isprime(num)):
    num += 1

# base_26 (base_10)
print(parse_string(num) + " (" + str(num) + ")")
