from math import *

clA = [[], []]
for s in open('27/27A_27780.txt'):
    s = s.replace(',', '.')
    x, y = [float(d) for d in s.split()]
    if y > 15:
        clA[0].append([x, y])
    else:
        clA[1].append([x, y])
print([len(cl) for cl in clA])


def center(cl):
    m = []
    for p in cl:
        s = sum([dist(p, p1) for p1 in cl])
        m.append([s, p])
    return min(m)[1]


cen = [center(cl) for cl in clA]
print((dist(cen[0], [1, 1.5]) + dist(cen[1], [1, 1.5])) * 10000)

# B
clB = [[], [], []]
for s in open('27/27B_27780.txt'):
    s = s.replace(',', '.')
    x, y = [float(d) for d in s.split()]
    if y > 25:
        clB[0].append([x, y])
    elif x < 24:
        clB[1].append([x, y])
    else:
        clB[2].append([x, y])
print([len(cl) for cl in clB])

cen = [center(cl) for cl in clB]
k = 0
for p in clB[1]:
    if dist(p, cen[1]) <= 1.2 and p != cen[1]:
        k += 1
print(k)

a = []
for p in clB[0]:
    if p != cen[0]:
        a.append(dist(cen[0], p))
print(min(a) * 10000)