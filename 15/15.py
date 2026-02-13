def f(x, y):
    return (2*x + y != 150) or (50<=x<=70) or (A > y)

for A in range(0, 1000):
    if all(f(x, y) == 1 for x in range(1000) for y in range(1000)):
        print(A)
        break