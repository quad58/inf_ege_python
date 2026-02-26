#5
# for n in range(1000):
#     s = bin(n)[2:]
#     if n % 2 == 0:
#         s += "0" * s.count("0")
#     elif n % 2 != 0:
#         s = "1" * s.count("1") + s
#     r = int(s, 2)
#     if r > 2000:
#         print(n)
#         break

#6
# import turtle as t
# t.screensize(3000, 3000)
# t.tracer(0)
# r = 30

# for i in range(6):
#     t.forward(7*r); t.right(120)

# t.up()
# t.forward(3*r); t.right(90)
# t.down()

# for i in range(8):
#     t.forward(5*r); t.right(90)

# t.up()
# for x in range(-50, 50):
#     for y in range(-50, 50):
#         t.goto(x*r, y*r); t.dot(5)

# t.done()

#7
# print(50 * 1024 * 1024 * 8 / (44100 * 32 * 2) / 60)

#8
# from itertools import *

# k = 0
# for s in permutations("КАБИНЕТ"):
#     s = ''.join(s)
#     if s[-1] not in "АИЕ":
#         k += 1
# print(k)

#9
# f = open("9.csv")

# k = 0
# for s in f:
#     a = [int(x) for x in s.split(";")]
#     a.remove(max(a))
#     a.remove(min(a))
#     r = sum(a) / len(a)
#     if r >= 8:
#         k += 1
# print(k)

#11
# from math import *
# c = ceil(log2(7))
# kod = ceil(8 * c / 8) + 8
# print(kod * 42)

# 13
# from ipaddress import *
# net = ip_network("192.168.76.160/255.255.255.240", 0)
# k = 0
# for ip in net:
#     s = bin(int(ip))[2:]
#     print(s, s[-8:])
#     if s[-1] == "0" and s[-8:].count("1") % 2 == 0:
#         k += 1
# print(k)

# 14
# def ch(n):
#     s = ""
#     while n > 0:
#         s = str(n%4) + s
#         n //= 4
#     return s

# r = ""
# for i in range(199, 0, -1):
#     s = ch(i)
#     if s[-3:] == "123":
#         r += str(i)
# print(r)

# 15
# def f(As, Ae, x):
#     return (As <= x <= Ae) <= ((101 <= x <= 143) or (144 <= x <= 199))

# a = []
# for As in range(1000):
#     for Ae in range(1, 1000):
#         if all(f(As, Ae, x) == 1 for x in range(1000)):
#             a.append(Ae - As)
# print(max(a))

# 16
# from functools import *

# @lru_cache(None)
# def f(n):
#     if n >= 2024:
#         return 1
#     else:
#         return f(n+2) + f(n+4)

# for i in range(2025, 1, -1):
#     f(i)

# a = set()
# for i in range(1, 2025):
#     a.add(f(i))
# print(len(a))

# 17
# def sm(s):
#     return sum(int(x) for x in str(abs(s)))

# a = [int(x) for x in open("17.txt")]
# b = []
# c = []

# for i in range(len(a)):
#     if 100 <= abs(a[i]) <= 999:
#         b.append(a[i])

# for i in range(len(a) - 1):
#     if ((sm(a[i]) % 5 == 0) + (sm(a[i+1]) % 5 == 0)) == 1 and abs(a[i] ** 2 - a[i+1] ** 2) >= max(b) ** 3:
#         c.append(a[i] + a[i+1])
    
# print(len(c), max(c))

# 19
# def f(a, b, m):
#     if a + b >= 183:
#         return m % 2 == 0
#     if m == 0:
#         return 0
#     h = [f(a+b, b, m-1), f(a, b+a, m-1), f(max(a, b), max(a, b), m-1)]
#     return any(h) if (m%2)-1 == 0 else all(h)
# print(19, [s for s in range(1, 184) if f(5, s, 2)])
# print(19, [s for s in range(1, 184) if (not f(5, s, 1)) and f(5, s, 3)])
# print(19, [s for s in range(1, 184) if (not f(5, s, 2)) and f(5, s, 4)])

# 23
# def sm(s):
#     return sum(int(x) for x in str(abs(s)))
# def f(x, y):
#     if x < y: return 0
#     if x == y: return 1
#     if x > y: return f(x - int(str(x**2)[0]), y) + f(x - sm(x), y)

# print(f(32, 1))

# 25
# from fnmatch import *

# k = 0
# for x in range(10**10+1, 0, -1):
#     if x % 42 == 0 and fnmatch(str(x), "48*15*0"):
#         print(x, x//42)
#         k += 1
#         if k == 5:
#             break
# 8 минут
        
# 2
# print("x y z w f")
# for x in 0, 1:
#     for y in 0, 1:
#         for z in 0, 1:
#             for w in 0, 1:
#                 f = ((1 == w) == (not ((w and x) or y))) <= z
#                 if x == 0 and y == 0 and f == 1:
#                     print(x, y, z, w, int(f))
# xzyw