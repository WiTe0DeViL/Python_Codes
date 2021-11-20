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
    for j in range(c):
        print(matrix[i][j], end=" ")
    print()
