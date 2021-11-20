a = list(input("Enter the string to remove Duplicates : \n"))

result = []
for i in a:
    if i not in result:
        result.append(i)

for x in result:
    print(x, end="")