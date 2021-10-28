import cmath

# get values as input 
a = int(input("a : "))
b = int(input("b : "))
c = int(input("c : "))


# Formula x = −b + √(b^2 − 4ac)/2a
# center part b^2-4ac

d = (b**2) - (4*a*c)

s1 = (-b + cmath.sqrt(d))/(2*a)
s2 = (-b - cmath.sqrt(d))/(2*a)

print(f"The Solutions are {s1} and {s2}")