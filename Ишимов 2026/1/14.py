for x in range(2030):
    a = 4 ** 100 - x
    k = 0
    while a > 0:
        if a % 4 == 0:
            k += 1
        a //= 4
    if k == 3:
        print(x)
        break