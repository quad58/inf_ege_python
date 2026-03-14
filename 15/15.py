#
# def f(x, y):
#     return (2*x + y != 150) or (50<=x<=70) or (A > y)

# for A in range(0, 1000):
#     if all(f(x, y) == 1 for x in range(1000) for y in range(1000)):
#         print(A)
#         break

#
# def f(x):
#     return((x%34==0) and (x%51!=0)) <= ((x%a!=0) or (x%51 ==0))
# for a in range(1,1000):
#     if all(f(x) == 1 for x in range(1,1000)):
#         print(a)
#         break

#
# from itertools import *
# def f(x):
#     b = 18<=x<=52
#     c = 16<=x<=41
#     a = a1<=x<=a2
#     return (b <= a) and (not c or a)
# ox = [i/4 for i in range(16 *4, 52*4+1)]
# m = []
# for a1,a2 in combinations(ox,2):
#     if all(f(x) == 1 for x in ox):
#         m.append(a2-a1)
# print(min(m))

# 4972
# from itertools import *

# def f(x):
#     P = 25 <= x <= 50
#     Q = 54 <= x <= 75
#     A = a1 <= x <= a2
#     return (Q) <= (((P) == (Q)) or ((not P) <= (A)))

# Ox = [i/4 for i in range(25 * 4, 75 * 4 + 1)]
# m = []
# for a1, a2 in combinations(Ox, 2):
#     if all(f(x) == 1 for x in Ox):
#         m.append(a2-a1)
# print(min(m))

# 
# from itertools import *

# def f(x):
#     P = 7 <= x <= 16
#     Q = 25 <= x <= 32
#     A = a1 <= x <= a2
#     return ((P) <= (A)) or (not (Q) <= (A))

# Ox = [i/4 for i in range(7*4, 32*4+1)]
# m = []
# for a1, a2 in combinations(Ox, 2):
#     if all(f(x) == 1 for x in Ox):
#         m.append(a2-a1)
# print(min(m))

# 
# from itertools import *

# def f(x):
#     P = 1 <= x <= 9999
#     Q = 3648 <= x <= 6287
#     A = a1 <= x <= a2
#     return ((P) == (Q)) or (A) or (x > 4200)

# Ox = [i/4 for i in range(1*4, 9999*4+1)]
# m = []
# for a1, a2 in combinations(Ox, 2):
#     if all(f(x) == 1 for x in Ox):
#         m.append(a2-a1)
# print(min(m))

# 20961
from itertools import *

def f(x):
    P = 15 <= x <= 142
    Q = 38 <= x <= 167
    A = a1 <= x <= a2
    return not (Q <= ((not A and P) <= (not Q)))

Ox = [i/4 for i in range(15 * 4, 167 * 4 + 1)]
m = []
for a1, a2 in combinations(Ox, 2):
    if all(f(x) == 0 for x in Ox):
        m.append(a2 - a1)
print(min(m))