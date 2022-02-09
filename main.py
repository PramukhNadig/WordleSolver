#!/bin/python3
##############################################################
# Create rankings based on usage of word using sigmoid function
# Use letters and somehow allow for duplicate letters, (maybe don't allow for duplicate letters until search space is small enough)
# Get list of words lol
#figure out GUI
import math

wordsAndFreq = {}
lettersInWord = []
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
    lettersInWord.append(letter)
    for word in wordsAndFreq.copy().keys():
        if((word[position] == letter) or (letter not in word)):
            del wordsAndFreq[word]

def update():
    for word in wordsAndFreq.copy().keys():
        for i in range(len(lettersInWord)):
            if(lettersInWord[i] in word):
                word = word.replace(lettersInWord[i], "", 1)


def sigmoid(word):
    return (1/(1+pow(math.e, )))

def main():
    setup()
    countWords()
    takeOutLetterG('f')
    takeOutLetterG('l')
    takeOutLetterG('a')
    takeOutLetterG('n')
    takeOutLetterG('k')   
    takeOutLetterG('w')
    takeOutLetterG('h')
    takeOutLetterG('i')
    takeOutLetterG('c')
    takeOutLetterG('h')    
    takeOutLetterG('g')
    takeOutLetterY('r', 2)
    takeOutLetterG('o')
    takeOutLetterG('u')
    takeOutLetterG('p')
    takeOutLetterY('e', 1)
    takeOutLetterG('v')
    takeOutLetterY('e', 3)
    takeOutLetterY('r', 4)
    takeOutLetterG('y')


    sorted(wordsAndFreq.keys())
    print(wordsAndFreq)

if __name__ == "__main__":
    main()