#!/bin/python3
##############################################################
# Create rankings based on usage of word using sigmoid function
# Use letters and somehow allow for duplicate letters, (maybe don't allow for duplicate letters until search space is small enough)
# Get list of words lol
#figure out GUI
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

def main():
    setup()
if __name__ == "__main__":
    main()