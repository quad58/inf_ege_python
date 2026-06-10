f = open("Ишимов 2026/1/9.csv")

k = 0
for s in f:
    a = [int(x) for x in s.split(";")]
    if len(set(a)) == len(a) and min(a) + max(a) < sum(a) - min(a) - max(a):
        k += 1
print(k)