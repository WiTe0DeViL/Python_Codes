a = list(input("Enter the string to remove Duplicates : \n"))

res = []
for i in a:
    if i not in res:
        res.append(i)

for x in res:
    print(x, end="")