#5360
from itertools import *

s = "37 367 125 56 34 247 126".split()
v = "AD DE EG GC CF FA FB AB BE".split()
print("1 2 3 4 5 6 7")
for p in permutations("ABCDEFG"):
    if all(str(p.index(a) + 1) in s[p.index(b)] for a, b in v:
        print(*p)