# Random odd and even number


from random import randint as r

def random_odd(a, b):
    num = r(a, b)
    while num % 2 == 0:
        num += 1

    return num

def random_even(a, b):
    num = r(a, b)
    if num % 2 == 0:
        return num
    else:
        return num+1


a = int(input("Enter the starting number : "))
b = int(input("Enter the Ending number : "))


print(random_even(a, b))
print(random_odd(a, b))