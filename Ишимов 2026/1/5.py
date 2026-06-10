a = []
for n in range(1000):
    s = bin(n)[2:]
    if s.count("1") % 2 == 0:
        s += "0"
        s = "111" + s[3:]
    elif s.count("1") % 2 != 0:
        s += "1"
        s = "10" + s[2:]
    r = int(s, 2)
    if r > 58:
        a.append(n)
print(min(a))