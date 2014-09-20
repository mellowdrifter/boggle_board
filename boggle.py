#!/usr/bin/python

'''
 CUBES:
 ======
 New Version | Old Version
 AAEEGN      | AACIOT
 ELRTTY      | AHMORS
 AOOTTW      | EGKLUY
 ABBJOO      | ABILTY
 EHRTVW      | ACDEMP
 CIMOTV      | EGINTV
 DISTTY      | GILRUW
 EIOSST      | ELPSTU
 DELRVY      | DENOSW
 ACHOPS      | ACELRS
 HIMNQU      | ABJMOQ
 EEINSU      | EEFHIY
 EEGHNW      | EHINPS
 AFFKPS      | DKNOTU
 HLNNRZ      | ADENVZ
 DEILRX      | BIFORX
'''

import random

game_type_new=''
letters=[]
boggle_letters=[]

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
for i in range(0,16):
    print boggle_letters[i]+"  ",
    if i==3 or i==7 or i==11:
        print"\n"


