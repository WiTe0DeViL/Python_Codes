import datetime as t
from time import sleep as s 
import sys


def typeText(text):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        s(0.10)

a = t.datetime.now()

typeText("Time Enna theriyuma seri iru na pathu Solra\n")

s(3)
typeText("Time oda Datum sollava...... iru\n")

s(3)

typeText(a.strftime("%Y-%m-%d %H-%M-%S"))
