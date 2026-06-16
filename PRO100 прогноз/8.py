from itertools import *

i = 0
for s in product(sorted("КОМПЬЮТЕР"), repeat=5):
    i += 1
    if i % 2 != 0 and s[0] != "Ь" and s.count("М") == 2:
        print(i)