#25355

f = [0] * 300000
g = [0] * 300000

for n in range(299999, 0, -1):
    if n >= 248045:
        g[n] = n / 20 + 28
    if n < 248045:
        g[n] = g[n + 9] - 4

for n in range(300000):
    if n >= 19:
        f[n] = f[n - 4] + 3580
    if n < 19:
        f[n] = 6 * (g[n - 7] - 36)

print(f[673])