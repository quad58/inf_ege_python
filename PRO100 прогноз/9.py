f = open("PRO100 прогноз/9.csv")

def sm(a):
    for x in range(4):
        for y in range(4):
            if x != y:
                if a[x] + a[y] == sum(a) - (a[x] + a[y]):
                    return False
    return True

k = 0
for s in f:
    a = [int(x) for x in s.split(";")]
    if sm(a) and max(a) < sum(a) - max(a):
        k += 1
print(k)