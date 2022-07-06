su = [80,
96,
18,
73,
78,
60,
60,
15,
45,
15,
10,
5,
46,
87,
33,
60,
14,
71,
65,
2,
5,
97,
0]
l=[]


# for n in range(len(su)):
#     for i in range(1,5):
#         if su[n]%5 == i:
#             if su[n] == 33:
#                 l.append(su[n])
#             elif su[n]+abs(i-5) - su[n] < 3:
#                 l.append(su[n]+abs(i-5))
#             else:
#                  l.append(su[n])



def gradingStudents(su):
    l = []
    for n in range(len(su)):
        for i in range(0,5):
            if su[n]%5 == i:
                if su[n] <= 33:
                    l.append(su[n])
                elif su[n]+abs(i-5) - su[n] < 3:
                    l.append(su[n]+abs(i-5))
                elif su[n]+abs(i-5) - su[n] > 3 or su[n]+abs(i-5) - su[n] == 3:
                    l.append(su[n])
    return l

print(gradingStudents(su))