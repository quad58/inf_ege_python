#
def f(x, y):
    return (2*x + y != 150) or (50<=x<=70) or (A > y)

for A in range(0, 1000):
    if all(f(x, y) == 1 for x in range(1000) for y in range(1000)):
        print(A)
        break

#
def f(x):
    return((x%34==0) and (x%51!=0)) <= ((x%a!=0) or (x%51 ==0))
for a in range(1,1000):
    if all(f(x) == 1 for x in range(1,1000)):
        print(a)
        break

#
from itertools import *
def f(x):
    b = 18<=x<=52
    c = 16<=x<=41
    a = a1<=x<=a2
    return (b <= a) and (not c or a)
ox = [i/4 for i in range(16 *4, 52*4+1)]
m = []
for a1,a2 in combinations(ox,2):
    if all(f(x) == 1 for x in ox):
        m.append(a2-a1)
print(min(m))