#!c:/Users/V1CT0R/AppData/Local/Programs/Python/Python310/python.exe
import sympy as sp
from sympy import *
import re


# (x)/(x+b)=(dx)/(a)

print("Formate = (x)/(x+b)=(dx)/(a)".center(40,"-"))

equation = input("\n Enter the equation : ")

def Chek(use=equation):
    if not re.match("x\/(\(x\+\d+\)|\(\d+\+x\))\s*=\s*((\(\d+x\)|\(x\d+\))|(\d+x|x\d+))\/\d+", use):
        print("Chek your Input format to find x\n example x/(x+b)=(dx)/a")
    else:
        print('\nEquation correct')
        return use.split('=')

    



def Solution(check):
    if check is None:
        pass
    else:
        ls = []
        pattern = re.compile("\d+")
        for i in range(0,2):
            ls.append(pattern.findall(check[i]))
        b,d,a,x = sp.symbols('b d a x')
        eq = sp.Eq(a*(x)/(x+b)*(x+b), a*(d*x)/a*(x+b))

        ex_qp = sp.expand(eq)

        res = ex_qp.subs([(b,ls[0][0]), (d,ls[1][0]),(a,ls[1][1])])
        print(f"\nEquation solution : {sp.solve(res,x)}")
        print(f"\nEquation result   : {sp.solve(ex_qp, x)}")

check = Chek(use=equation)
Solution(check)