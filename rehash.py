'''
Hashes a string in sha1,
and then rehashes the hash until it
contains the original string
'''

from common import sha1_b64

desire = input("What to hash? ")
desire = desire.split(" ")

max_hash = int(input("Max hash num? "))

curr = sha1_b64(desire[0])

count = 0

def search(name):
    global curr
    global count
    
    while(name not in curr):
        if(curr == "reset!"):
            curr = sha1_b64(name)
        
        curr = sha1_b64(curr)
        count += 1

        if(count > max_hash):
            count = 0
            curr = "reset!"
            break

for name in desire:
    search(name)

    if(curr != "reset!"):
        print(curr)
        print("It took " + str(count) + " iterations to find that")
