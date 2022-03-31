#!/bin/python3
##############################################################
# Create rankings based on usage of word using sigmoid function
# Use letters and somehow allow for duplicate letters, (maybe don't allow for duplicate letters until search space is small enough) DONE
# Get list of words DONE
#figure out GUI

#tweak takeoutletterG such that duplicates are handled.
import math
import itertools
from webbrowser import get
wordsAndFreq = {}
lettersInWord = set()
class Color():
    GREEN=2
    YELLOW=1
    GRAY=0

def setup():
    freq = open('words.txt', 'r+')
    lines = freq.readlines()
    freq.seek(0)
    count = 0
    for line in lines:
        line = str(line)
        l = line.split(' ')
        if(len(l[0]) == 5):
            freq.write(line)
    freq.truncate()
    freq.close()

def countWords():
    freq = open('words.txt', 'r+')
    lines = freq.readlines()
    freq.seek(0)
    count = 0
    for line in lines:
        line = str(line)
        l = line.split(' ')
        wordsAndFreq[l[0]] = int(l[1].strip())
    print(wordsAndFreq.get("first"))

def takeOutLetterG(letter):        
    for word in wordsAndFreq.copy().keys():
        if(letter in word):
            del wordsAndFreq[word]

def takeOutLetter(letter, position):
    position = position -1
    if((letter == 'l') and (position == 3)):
        print(letter)
    if(letter not in lettersInWord):
        takeOutLetterG(letter)
    else:
        for word in wordsAndFreq.copy().keys():
            if((word[position] == letter)):
                del wordsAndFreq[word]

def takeOutLetterY(letter, position):
    position = position -1
    for word in wordsAndFreq.copy().keys():
        if((word[position] == letter) or (letter not in word)):
            del wordsAndFreq[word]

def takeOutLetterGR(letter, position):
    position = position -1
    for word in wordsAndFreq.copy().keys():
        if(not(word[position] == letter)):
            del wordsAndFreq[word]

def getWordArray(word, colors):
    for i in range(len(colors)):
        if(colors[i] == 1 or colors[i] == 2):
            lettersInWord.add(word[i])
    for i in range(len(word)):
        if(colors[i] == Color.GREEN):
            takeOutLetterGR(word[i], i+1)
        elif(colors[i] == Color.GRAY):
            takeOutLetter(word[i], i+1)
        elif(colors[i] == Color.YELLOW):
            takeOutLetterY(word[i], i+1)
    printTop10()
    return wordsAndFreq

def printTop10():
    sorted(wordsAndFreq.values())
    arr = list(wordsAndFreq.keys())
    print((arr[:10]))




def getAllPermutationsColors():
    arr = [[]]
    colors = [Color.GRAY, Color.YELLOW, Color.GREEN]

    for i in colors:
        for j in colors:
            for k in colors:
                for l in colors:
                    for m in colors:
                        arr.append([i, j, k, l, m])
    return arr


def main():
    setup()
    countWords()
    print(len(getAllPermutationsColors()))

    getWordArray('crane', [0,0,0,0,2])
    getWordArray('house', [0,2,0,0,2])
    getWordArray('movie', [0,2,0,0,2])
    getWordArray('lodge', [0,2,2,2,2])

if __name__ == "__main__":
    main()
