# 25707
from math import *
for n in range(1, 10000):
    char = ceil(log2(n))
    pas = 11*char/8 + 40
    if 3000 * pas >= 170 * 1024:
        print(n)
        break