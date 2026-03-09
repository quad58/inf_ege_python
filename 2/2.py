#k 1623
# from itertools import *

# def f(x, y, z):
#     return ((not x) or (not z)) <= (x == y)

# for a1, a2, a3 in product([0, 1], repeat=3):
#     t = [(1, a1, 1), (a2, a3, 1)]
#     if len(t) == len(set(t)):
#         for p in permutations("xyz"):
#             if [f(**dict(zip(p, row))) for row in t] == [0, 0]:
#                 print(*p)

#k 6708
from itertools import *

def f(x, y, z, w):
    return (y <= x) and (not z) and w

for a1, a2, a3, a4, a5, a6 in product([0, 1], repeat=6):
    t = [(1, 0, a1, a2), (1, 1, a3, a4), (a5, 1, 1, a6)]
    if len(t) == len(set(t)):
        for p in permutations("xyzw"):
            if [f(**dict(zip(p, rows))) for rows in t] == [1, 1, 1]:
                print(*p)