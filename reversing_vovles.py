def revvov(s):
    char = list(s)
    index = []
    vov = []
    final = []
    ind = 0
    for i in range(len(s)):
        if char[i] in ['a','e','i','o','u']:
            vov.append(s[i])
            index.append(i)
    vov = vov[::-1]
    for i in range(len(char)):
        if i in index:
            final.append(vov[ind])
            ind+=1
        else:
            final.append(char[i])
    print(''.join(final))
    print(index,vov)

revvov('surenkumar')


