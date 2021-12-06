import os
import sys
from time import sleep as s

def typeText(text):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        s(0.10)

def typeInput(text):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        s(0.10)
    value = input()
    return value

def cls():
    os.system("cls")


typeText("Hey Buddy")
s(1)
typeText("\nAre you a boy")
s(1)
Boy = typeInput("\nGive us B if your a boy G for Girl and O for Other 😊")
s(1)
if Boy == "B":
    typeText("Dear Boys Life is Limited "
             "\nBut Girls are Unlimited "
             "\nSo Don't follow Girls"
             "\nFollow Your Goals")

elif Boy == "G":
    typeText("Hi girls please stay away plz....")

elif Boy == "O":
    typeText("Its a Pleasure to meeting You"
             "\nYour being Positive and continue being"
             "\nan inspiration for Other")

else:
    typeText("\nDon't be a SUCKER")
s(1)
typeText("\nOk Bye\n")
s(1)
typeText("I'm gonna vanish in 3..")
s(1)
typeText("2..")
s(1)
typeText("1..\n")
s(2)
typeText("hehehehe......\n")
s(1)
typeText("Ok Byeee....")
cls()
