from math import *

for n in range(1, 1000):
    char = ceil(log2(n))
    pas = 1224*char/8
    if 16535 * pas <= 13 * 1024 * 1024:
        print(n)