#!/usr/bin/python

import random
import time
import sys

class colours:
    def __init__(self):
        self.green = "\033[92m"
        #self.blue = "\033[94m"
        #self.bold = "\033[1m"
        #self.yellow = "\033[93m"
        self.red = "\033[91m"
        self.end = "\033[0m"
ga = colours()

def printBoard(x):
    print "\nHere is your board:\n"
    edge=ga.red+"+-------+-------+-------+-------+"+ga.end
    print edge
    for i in range(0,4):
        if "Q" in boggle_letters[i]:
           print ga.red+"|   "+ga.end+""+ga.green+boggle_letters[i]+"u"+ga.end+" ",
        else:
            print ga.red+"|   "+ga.end+""+ga.green+boggle_letters[i]+ga.end+"  ",
    print ga.red+"|"+ga.end
    print edge
    for i in range(4,8):
        if "Q" in boggle_letters[i]:
            print ga.red+"|   "+ga.end+""+ga.green+boggle_letters[i]+"u"+ga.end+" ",
        else:
            print ga.red+"|   "+ga.end+""+ga.green+boggle_letters[i]+ga.end+"  ",
    print ga.red+"|"+ga.end
    print edge
    for i in range(8,12):
        if "Q" in boggle_letters[i]:
            print ga.red+"|   "+ga.end+""+ga.green+boggle_letters[i]+"u"+ga.end+" ",
        else:
            print ga.red+"|   "+ga.end+""+ga.green+boggle_letters[i]+ga.end+"  ",
    print ga.red+"|"+ga.end
    print edge
    for i in range(12,16):
        if "Q" in boggle_letters[i]:
            print ga.red+"|   "+ga.end+""+ga.green+boggle_letters[i]+"u"+ga.end+" ",
        else:
            print ga.red+"|   "+ga.end+""+ga.green+boggle_letters[i]+ga.end+"  ",
    print ga.red+"|"+ga.end
    print edge

def getLetters(x):
    boggle_letters=[]
    letters=[]
    for i in range(0,16):
        choice=random.randint(0,5)
        letters.append(x[i][choice])
    while len(letters)>0:
        choice=random.randint(0,len(letters)-1)
        boggle_letters.append(letters[choice])
        letters.pop(choice)
    return boggle_letters

def timer(x):
    width=x*30
    for i in range(0,3):
        sys.stdout.write("[%s]" % ("-" * 30))
        sys.stdout.flush()
        sys.stdout.write("\b" * 31)
        for i in range(0,30):
            sys.stdout.write("*")
            sys.stdout.flush()
            time.sleep(2)
        print"\n"
    print"\n\n\n\n\n\n\n\nTime's up! Put down your pens!\a"

if __name__ == "__main__":
    print """
    Welcome to Boggle. This game contains both the older tileset and newer tileset. Once the tileset
    has been selected, the game will randomise the letters. When complete you have the option of showing
    the board and start the three minute timer. When the timer is done, the computer will alert
    """
    game_type=raw_input("Please choose which tileset you'd like to use - (N/O)").lower()
    while game_type not in ["n","o"]:
        game_type=raw_input("Invalid response! Please choose which tileset you'd like to use - (N/O)").lower()

    if game_type == "n":
        squares=["AAEEGN","ELRTTY","AOOTTW","ABBJOO","EHRTVW","CIMOTV","DISTTY","EIOSST","DELRVY","ACHOPS","HIMNQU","EEINSU","EEGHNW","AFFKPS","HLNNRZ","DEILRX"]
    else:
        squares=["AACIOT","AHMORS","EGKLUY","ABILTY","ACDEMP","EGINTV","GILRUW","ELPSTU","DENOSW","ACELRS","ABJMOQ","EEFHIY","EHINPS","DKNOTU","ADENVZ","BIFORX"]

    raw_input("\nLetters randomised. Press any key to show the board and start the three minute timer...")
    boggle_letters=getLetters(squares)
    printBoard(boggle_letters)
    timer(3)


