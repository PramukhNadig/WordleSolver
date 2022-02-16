#!/bin/python3
##############################################################
# Create rankings based on usage of word using sigmoid function
# Use letters and somehow allow for duplicate letters, (maybe don't allow for duplicate letters until search space is small enough)
# Get list of words lol
#figure out GUI
import math
import itertools

wordsAndFreq = {}
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
    for word in wordsAndFreq.copy().keys():
        if(not(word[position] == letter)):
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
    for i in range(len(word)):
        if(colors[i] == Color.GREEN):
            takeOutLetterGR(word[i], i+1)
        elif(colors[i] == Color.GRAY):
            takeOutLetterG(word[i])
        elif(colors[i] == Color.YELLOW):
            takeOutLetterY(word[i], i+1)
    return wordsAndFreq

#take letter, remove all words that dont match from copy and return remaining size over total.
def calculateLikelihood(word, colors, arr):
    total = len(arr)
    arr1 = arr.keys().copy()
    for i in range(len(word)):
        if(colors[i] == Color.GREEN):
            for word in arr1.keys():
                if(not(word[i] == word[i])):
                    del wordsAndFreq[word]


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
    arr = getAllPermutationsColors()
    print(arr)
    setup()
    countWords()
    getWordArray('smart', arr[220])
    getWordArray('smrek', [2, 2, 1, 0, 0])
    sorted(wordsAndFreq.keys())
    print(wordsAndFreq)

if __name__ == "__main__":
    main()