'''
O god of wires, spirit of the bits -
show yourself amongst this code,
and brighten it through your presence
'''

'''
This code is for generating a sha1 hash containing a word,
using only japanese sounds (and space)
'''

from common import sha1_b64

chars = ["a", "e", "i", "o", "u", "ka", "ke", "ki", "ko", "ku", "n",
         "ha", "he", "hi", "ho", "fu", "sa", "shi", "su", "se", "so",
         "ta", "chi", "tsu", "te", "to", "na", "ni", "nu", "ne", "no", "ma",
         "mi", "mu", "me", "mo", "ya", "yu", "yo", "ra", "ri", "ru", "re",
         "ro", "wa", "wo", " "]

indexes = [0]

desire = input("what do you desire? ")

while True:
    indexes[0] += 1

    # for checking for carrying
    # (eg [3, max, 7] should become [3, 0, 8])
    for i in range(0, len(indexes)):
        if(indexes[i] >= len(chars) - 1):
            indexes[i] -= (len(chars) - 1)

            if(i + 1 == len(indexes)):
                indexes.append(0)
            else:
                indexes[i + 1] += 1

    word = ""

    for index in indexes:
        word += chars[index]
    
    jap_hash = sha1_b64(word)
    
    if(desire in jap_hash):
        print(word)
        print(jap_hash)
        break
