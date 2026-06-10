from itertools import *

n = 0
for s in product(sorted("КОФЕ"), repeat=5):
    s = "".join(s)
    n += 1
    if "Е" not in s and s.count("Ф") == 1:
        print(n)