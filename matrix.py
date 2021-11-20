from random import randint as ri

r = int(input("Enter the rows : "))
c = int(input("Enter the columns : "))

# matrix list
matrix = []
print("Enter the value for matrix row wise : ")

# creating matrix
for i in range(r):
    a = []
    for j in range(c):
        a.append(int(input()))
    matrix.append(a)

# displaying matrix
for i in range(r):
    st = "| "
    for j in range(c):
        if matrix[i][j] < 10:
            st += str(matrix[i][j]) + "  | "
        else:
            st += str(matrix[i][j]) + " | "
    print(st)

print("~~~~~~~~~Random Matrix~~~~~~~~~~~~")
print()

Random_matrix = []

# Random matrix
for i in range(r):
    b = []
    for j in range(c):
        b.append(ri(0, 99))
    Random_matrix.append(b)

# displaying Random_matrix
for i in range(r):
    st = "| "
    for j in range(c):
        if Random_matrix[i][j] < 10:
            st += str(Random_matrix[i][j]) + "  | "
        else:
            st += str(Random_matrix[i][j]) + " | "
    print(st)
