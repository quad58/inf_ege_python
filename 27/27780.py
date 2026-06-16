# from math import *

# clA = [[], []]
# for s in open('27/27A_27780.txt'):
#     s = s.replace(',', '.')
#     x, y = [float(d) for d in s.split()]
#     if y > 15:
#         clA[0].append([x, y])
#     else:
#         clA[1].append([x, y])
# print([len(cl) for cl in clA])


# def center(cl):
#     m = []
#     for p in cl:
#         s = sum([dist(p, p1) for p1 in cl])
#         m.append([s, p])
#     return min(m)[1]


# cen = [center(cl) for cl in clA]
# print((dist(cen[0], [1, 1.5]) + dist(cen[1], [1, 1.5])) * 10000)

# # B
# clB = [[], [], []]
# for s in open('27/27B_27780.txt'):
#     s = s.replace(',', '.')
#     x, y = [float(d) for d in s.split()]
#     if y > 25:
#         clB[0].append([x, y])
#     elif x < 24:
#         clB[1].append([x, y])
#     else:
#         clB[2].append([x, y])
# print([len(cl) for cl in clB])

# cen = [center(cl) for cl in clB]
# k = 0
# for p in clB[1]:
#     if dist(p, cen[1]) <= 1.2 and p != cen[1]:
#         k += 1
# print(k)

# a = []
# for p in clB[0]:
#     if p != cen[0]:
#         a.append(dist(cen[0], p))
# print(min(a) * 10000)

# 29081
# from math import *

# f = open("27/27_B_29357.txt")
# clB = [[], [], []]
# for s in f:
#     s = s.replace(",", ".")
#     x, y, t = [x for x in s.split()]
#     x = float(x)
#     y = float(y)
#     if x > 16:
#         clB[0].append([[x, y], t])
#     elif y < 30:
#         clB[1].append([[x, y], t])
#     else:
#         clB[2].append([[x, y], t])

# def center(cl):
#     m = []
#     for p in cl:
#         s = sum([dist(p[0], p1[0]) for p1 in cl])
#         m.append([s, p])
#     return min(m)[1]

# centr = [center(cl) for cl in clB]

# k1 = 0
# for p in clB[0]:
#     if "K" in p[1] and "III" in p[1]:
#         k1 += 1
# k2 = 0
# for p in clB[1]:
#     if "K" in p[1] and "III" in p[1]:
#         k2 += 1
# k3 = 0
# for p in clB[2]:
#     if "K" in p[1] and "III" in p[1]:
#         k3 += 1
# print(k1, k2, k3)

# d1 = []
# for p in clB[0]:
#     if "G" in p[1] and "V" in p[1]:
#         d1.append(p[0])
# d2 = []
# for p in clB[1]:
#     if "G" in p[1] and "V" in p[1]:
#         d2.append(p[0])
# d3 = []
# for p in clB[2]:
#     if "G" in p[1] and "V" in p[1]:
#         d2.append(p[0])

# r = [dist(p, p1) for p in d1 for p1 in d2] + [dist(p, p1) for p in d1 for p1 in d3] + [dist(p, p1) for p in d2 for p1 in d3];

# print(dist(centr[1][0], centr[0][0]) * 10000)
# print(max(r))
# B=[[],[],[]]
# for s in open('27/27_B_29357.txt'):
#     x,y,t = s.replace(',','.').split()
#     x,y = float(x), float(y)
#     if t=='VII': t='  VII'
#     if x>16: B[0].append([x,y,t])
#     elif y>30: B[1].append([x,y,t])
#     else: B[2].append([x,y,t])

# def dist(p1,p2):
#     x1,y1,t1 = p1
#     x2,y2,t2 = p2
#     return ((x2-x1)**2+(y2-y1)**2)**0.5

# def centr(cl):
#     m = []
#     for p in cl:
#         s = sum(dist(p,p1) for p1 in cl)
#         m.append([s,p])
#     return min(m)[1]

# b1 = dist(centr(B[0]),centr(B[2]))

# g0 = [p for p in B[0] if p[2][0]=='G' and p[2][2:]=='V']
# g1 = [p for p in B[1] if p[2][0]=='G' and p[2][2:]=='V']
# g2 = [p for p in B[2] if p[2][0]=='G' and p[2][2:]=='V']

# r = [dist(p,p1) for p in g0 for p1 in g0]+\
#     [dist(p,p1) for p in g1 for p1 in g1]+\
#     [dist(p,p1) for p in g2 for p1 in g2]
# b2 = max(r)

# print(int(b1*10000), int(b2*10000))

#k 9010
from math import *

f = open("27/27-113a.txt")
clA = [[], []]
for s in f:
    s = s.replace(",", ".")
    x, y = [float(d) for d in s.split()]
    if y > 15:
        clA[0].append([x, y])
    else:
        clA[1].append([x, y])

def center(cl):
    m = []
    for p in cl:
        s = sum([dist(p, p1) for p1 in cl])
        m.append([s, p])
    return min(m)[1]

cen = [center(cl) for cl in clA]

print(len(clA[0]), len(clA[1])) # 301

print((dist(cen[0], [-1.0, 1.3]) + dist(cen[1], [-1.0, 1.3]))*10000) # 319272

clB = [[], [], []]
for s in open("27/27-113b.txt"):
    s = s.replace(",", ".")
    x, y = [float(d) for d in s.split()]
    if y > 25:
        clB[0].append([x, y])
    elif x > 25:
        clB[1].append([x, y])
    else:
        clB[2].append([x, y])

cen = [center(cl) for cl in clB]

print(len(clB[0]), len(clB[1]), len(clB[2])) # 200

k = 0
for p in clB[2]:
    if dist(p, cen[2]) < 1.6 and p != cen[2]:
        k += 1
print(k)

dists = []
for p in clB[0]:
    dists.append(dist(cen[0], p))
print(max(dists) * 10000) # 26825