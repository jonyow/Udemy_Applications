
import json
from difflib import get_close_matches

data = json.load( open(r'C:\Users\2011940\PycharmProjects\Udemy_Applications\Data\data.json'))

def printDefinition(list):
    print("Definition: ")
    for item in list:
        print(item)

word = input("Enter word: ")
word = word.lower()

while word != 'exit':
    if word in data:
        printDefinition(data[word])
    else:
        nearest_match = get_close_matches(word, data.keys(), 1)[0]
        print("Word not found. Is this your what you meant: " + nearest_match)
        yn = input("Y/N?")

        if yn.lower() =='y':
            printDefinition(data[nearest_match])
        else:
            print("Try another word...")

    word = input("Enter word: ")
    word = word.lower()

help(json.load)

import numpy