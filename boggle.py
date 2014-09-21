#!/usr/bin/python

import random

class colors:
    def __init__(self):
        self.green = "\033[92m"
        self.blue = "\033[94m"
        self.bold = "\033[1m"
        self.yellow = "\033[93m"
        self.red = "\033[91m"
        self.end = "\033[0m"
ga = colors()

game_type_new=''
letters=[]
boggle_letters=[]

def printBoard(x):
    for i in range(0,16):
        print ga.green+boggle_letters[i]+ga.end+"  ",
        if i==3 or i==7 or i==11:
            print ga.red+"|\n"+ga.end

if game_type_new:
    squares=["AAEEGN","ELRTTY","AOOTTW","ABBJOO","EHRTVW","CIMOTV","DISTTY","EIOSST","DELRVY","ACHOPS","HIMNQU","EEINSU","EEGHNW","AFFKPS","HLNNRZ","DEILRX"]
else:
    squares=["AACIOT","AHMORS","EGKLUY","ABILTY","ACDEMP","EGINTV","GILRUW","ELPSTU","DENOSW","ACELRS","ABJMOQ","EEFHIY","EHINPS","DKNOTU","ADENVZ","BIFORX"]

for i in range(0,16):
    choice=random.randint(0,5)
    letters.append(squares[i][choice])

while len(letters)>0:
    choice=random.randint(0,len(letters)-1)
    boggle_letters.append(letters[choice])
    letters.pop(choice)

print "\nHere is your board:\n"
printBoard(boggle_letters)


