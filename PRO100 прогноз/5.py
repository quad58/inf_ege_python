for n in range(1000):
    s = bin(n)[2:]
    if n % 3 == 0:
        s += s[-3:]
    elif n % 3 != 0:
        s += bin((n % 3) * 3)[2:]
    r = int(s, 2)
    if 170 < r < 180:
        print(n, r)
# 43