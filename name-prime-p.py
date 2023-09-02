'''
Checks if a name as base 26 is prime
'''

from sympy.ntheory import isprime
from common import parse_number

while True:
    num = parse_number(input())
    
    if(isprime(num)):
        print("Jackpot (" + str(num) + ")")
    else:
        print("Not prime")
