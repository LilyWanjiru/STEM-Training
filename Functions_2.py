#Functions to replace characters in a string
from ctypes.wintypes import WORD


def replace_in (Phrase):
    word = ""
    for letter in Phrase:
        if letter.lower() in "aeiou":
            word = word + "g"
    else:
        word = word + letter
    return word
print (replace_in(input("Enter a phrase: ")))
