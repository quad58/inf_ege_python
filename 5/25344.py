# def tr(n):
#     s = ""
#     while n > 0:
#         s = str(n%3) + s
#         n //= 3
#     return s

# def sm(s):
#     m = 0
#     for c in s:
#         m += int(c)
#     return m

# for n in range(1, 1000):
#     s = tr(n)
#     if n % 3 == 0:
#         s += s[-2:]
#     if n % 3 != 0:
#         s += tr(sm(s) * 3)
#     r = int(s, 3)
#     if r % 2 != 0 and r > 208:
#         print(r)
#         break

# 24736
# def dv(n):
#     s = ""
#     while n > 0:
#         s = str(n%2) + s
#         n //= 2
#     return s

# for n in range(1, 1000):
#     a = dv(n)
#     if a.count("1") % 2 == 0:
#         a = a + "0"
#         a = "10" + a[2:]
#     elif a.count("1") % 2 != 0:
#         a = a + "1"
#         a = "11" + a[2:]
#     r = int(a, 2)
#     if n % 2 != 0 and r % 2 == 0 and r > 367:
#         print(n)
#         break

# 25138313_5
def db(s):
    a = ""
    for c in s:
        a += c
        a += c
    return a

def inv(s):
    a = ""
    for c in s:
        if c == "0":
            a += "1"
        else:
            a += "0"
    return a

for n in range(1000):
    s = bin(n)[2:]
    if n % 2 == 0:
        s = db(s)
    elif n % 2 != 0:
        s = inv(s)
        s = db(s)
    r = int(s, 2)
    if r > 60:
        print(n)
        break