# 25362
# def div(x):
#     s = set()
#     for i in range(2, int(x ** 0.5) + 1):
#         if x % i == 0:
#             s.add(i)
#             s.add(x//i)
#     return s

# k = 0
# for x in range(1_350_051, 10 ** 8):
#     d = div(x)
#     if len(d) > 0:
#         d = [y for y in d if y % 100 == 11 and y != x and y != 11]
#         if k < 5 and len(d) > 0:
#             print(x, min(d))
#             k += 1

# 23763
# def div(x):
#     s = set()
#     for i in range(2, int(x ** 0.5) + 1):
#         if x % i == 0:
#             s.add(i)
#             s.add(x//i)
#     return s

# k = 0
# for x in range(800000, 10000001):
#     d = div(x)
#     if len(d) > 0:
#         m = max(d) + min(d)
#         if m % 10 == 4 and k < 5:
#             print(x, m)
#             k += 1

# 23764
# from fnmatch import *

# for x in range(0, 10 ** 10 + 1, 1917):
#     if fnmatch(str(x), "3?12?14*5"):
#         print(x, x // 1917)

# 23207
# def div(x):
#     s = []
#     for i in range(1, int(x ** 0.5) + 1):
#         if x % i == 0:
#             s.append(i)
#             s.append(x//i)
#     return s

# k = 0
# for x in range(1_324_728, 10 ** 8):
#     d = div(x)
#     if len(d) == 4:
#         d = [y for y in d if y != 1 and y != x]
#         d = [y for y in d if len(div(y)) == 2 and str(y).count("5") == 1]
#         if k < 5 and len(d) == 2:
#             print(x, max(d))
#             k += 1

# 21909
# def div(x):
#     s = []
#     for i in range(1, int(x ** 0.5) + 1):
#         if x % i == 0:
#             s.append(i)
#             s.append(x//i)
#     return s

# k = 0
# for x in range(500000, 1000000):
#     d = div(x)
#     r = sum(d)
#     if r % 10 == 6 and k < 5:
#         print(x, r)
#         k += 1

# 21718
# from fnmatch import *

# for x in range(0, 10 ** 10, 7993):
#     if fnmatch(str(x), "4*4736*1"):
#         print(x, x // 7993)

# 23282
# def div(x):
#     s = set()
#     for i in range(1, int(x ** 0.5) + 1):
#         if x % i == 0:
#             s.add(x)
#             s.add(x//i)
#     return s

# k = 0
# for x in range(5_400_001, 10 ** 8):
#     d = div(x)
#     if len(d) > 2:
#         d = [y for y in d if len(div(y)) == 2]
#         if len(d) > 0:
#             m = max(d) + min(d)
#             if m > 60000 and str(m) == str(m)[::-1] and k < 5:
#                 print(x, m)
#                 k += 1

# 24896
# def div(x):
#     s = set()
#     for i in range(2, int(x ** 0.5) + 1):
#         if x % i == 0:
#             s.add(x)
#             s.add(x//i)
#     return s

# def p(x):
#     return x > 1 and all(x%i != 0 for i in range(2, int(x ** 0.5) + 1))

# k = 0
# for x in range(1_474_999, 0, -1):
#     if k == 5: break
#     d = [y for y in div(x) if p(y) == 1]
#     s = sum(d)
#     if s != 0 and s <= 42000 and s % 6 == 0:
#         print(x, s)
#         k += 1

# def div(x):
#     d = set()
#     for i in range(2, int(x**0.5) + 1):
#         if x % i == 0:
#             d |= {i, x//i}
#     return sorted(d)

# def p(x):
#     return x > 1 and all(x % i != 0 for i in range(2, int(x ** 0.5) + 1))

# k = 0
# for x in range(1_474_999, 1_000_000, -1):
#     if k == 5: break
#     d = [i for i in div(x) if p(i) == 1]
#     s = sum(d)
#     if s != 0 and s < 42_000 and s % 6 == 0:
#         print(x, s)
#         k += 1

# 26557
# def div(x):
#     d = set()
#     for i in range(2, int(x ** 0.5) + 1):
#         if x % i == 0:
#             d |= {i, x//i}
#     return d

# def p(x):
#     return x > 1 and all(x % i != 0 for i in range(2, int(x ** 0.5) + 1))

# k = 0
# for x in range(7_800_000, 10 ** 8):
#     d = [x for x in div(x) if p(x) == 1]
#     if len(d) > 0:
#         m = min(d) + max(d)
#         if m % 100 == 63 and m % len(d) == 0 and k < 5:
#             print(x, m)
#             k += 1

# 22430
# def div(x):
#     d = set()
#     for i in range(2, int(x ** 0.5) + 1):
#         if x % i == 0:
#             d |= {i, x//i}
#     return sorted(d)

# def p(x):
#     return x > 1 and all(x % i != 0 for i in range(2, int(x ** 0.5) + 1))

# k = 0
# for x in range(456_789, 10 ** 7):
#     d = [y for y in div(x) if p(y) == 1]
#     m = 0
#     if len(d) >= 4:
#         m = d[0] + d[1] + d[-1] + d[-2]
#     if m % 114 == 39 and k < 5:
#         print(x, m)
#         k += 1

# 19776
# def div(x):
#     d = set()
#     for i in range(2, int(x ** 0.5) + 1):
#         if x % i == 0:
#             d |= {i, x//i}
#     return d

# def p(x):
#     return x > 1 and all(x % i != 0 for i in range(2, int(x ** 0.5) + 1))

# k = 0
# for x in range(23_600_000, 10 ** 10):
#     if k == 6: break
#     d = [x for x in div(x) if p(x) == 1]
#     if len(d) > 0:
#         m = min(d) + max(d)
#         if m % 213 == 171:
#             print(x, m)
#             k += 1

# 19775
# def div(x):
#     d = set()
#     for i in range(2, int(x ** 0.5) + 1):
#         if x % i == 0:
#             d |= {i, x//i}
#     return d

# def p(x):
#     return x > 1 and all(x % i != 0 for i in range(2, int(x ** 0.5) + 1))

# k = 0
# for x in range(32_500_000, 10 ** 10):
#     if k == 7: break
#     d = [x for x in div(x) if p(x) == 1]
#     s = 0
#     if len(d) > 0:
#         s = sum(d)
#         if s != 0 and s % 145 == 0:
#             print(x, s)
#             k += 1

# 20541
# from fnmatch import *

# for x in range(0, 10 ** 9, 4321):
#     if fnmatch(str(x), "34*56?7"):
#         s = 1
#         for c in str(x):
#             s *= int(c)
#         print(x, s)

# 14440
# from fnmatch import *

# def p(x):
#     return x > 1 and all(x % i != 0 for i in range(2, int(x ** 0.5) + 1))

# for x in range(0, 10 ** 7):
#     if fnmatch(str(x), "31*567?") and p(x) == 1:
#         s = 1
#         for c in str(x):
#             s *= int(c)
#         print(x, s)

#k 8394
# def p(x):
#     d = []
#     i = 2
#     while i * i <= x:
#         while x % i == 0:
#             d.append(i)
#             x = x // i
#         i += 1
#     if x > 1:
#         d.append(x)
#     return d

# for x in range(13_475_124, 13_500_000):
#     d = p(x)
#     if len(d) == 5 and "5" in str(d[0]) and "5" in str(d[1]) and "5" in str(d[2]) and "5" in str(d[3]) and "5" in str(d[4]):
#         print(x, max(d))

#k 8313
# def p(x):
#     d = []
#     i = 2
#     while i * i <= x:
#         while x % i == 0:
#             d.append(i)
#             x = x // i
#         i += 1
#     if x > 1:
#         d.append(x)
#     return d

# k = 0
# for x in range(2_700_034, 3_000_000, 100):
#     if k == 5: break
#     d = p(x)
#     d1 = [i for i in d if d.count(i) >= 5]
#     if len(d1) > 0:
#         print(x, min(d1))
#         k += 1

#k 8365
# def p(x):
#     d = []
#     i = 2
#     while i * i <= x:
#         while x % i == 0:
#             d.append(i)
#             x = x // i
#         i += 1
#     if x > 1:
#         d.append(x)
#     return d

# for x in range(700_000, 1_000_000):
#     d = p(x)
#     if len(d) > 1 and len(set(d)) == 1:
#         print(x, d[0])

#k 5227
# def div(x):
#     d = set()
#     for i in range(2, int(x ** 0.5) + 1):
#         if x % i == 0:
#             d.add(i)
#             d.add(x//i)
#     return sorted(d)

# i = 0
# for k in range(1, 10000):
#     if i == 5: break
#     N = 500_000_000 + k
#     d = div(N)
#     if len(d) < 3:
#         print(k, N, d)
#         i += 1

# 26536
# def p(x):
#     d = []
#     i = 2
#     while i * i <= x:
#         while x % i == 0:
#             d.append(i)
#             x = x // i
#         i += 1
#     if x > 1:
#         d.append(x)
#     return d

# k = 0
# for x in range(3_502_101, 4_000_000):
#     if k == 5: break
#     d = p(x)
#     if len(d) == 4 and any(b for b in d if str(b) == str(b)[::-1] and len(str(b)) == 2):
#         print(x, max(d))
#         k += 1

# 26680
# def fact(x):
#     d = []
#     i = 2
#     while i * i <= x:
#         while x % i == 0:
#             d.append(i)
#             x = x // i
#         i += 1
#     if x > 1:
#         d.append(x)
#     return d

# def pr(x):
#     return x > 1 and all(x % i != 0 for i in range(2, int(x ** 0.5) + 1))

# for x in range(5_000_001, 6_000_000):
#     d = fact(x)
#     d1 = [c for c in d if c % 2 != 0]
#     if len(d) == 2 and d == d1 and pr(d1[1] - d[0]):
#         print(x, max(d1))

# 26682
# def fact(x):
#     d = []
#     i = 2
#     while i * i <= x:
#         while x % i == 0:
#             d.append(i)
#             x = x // i
#         i += 1
#     if x > 1:
#         d.append(x)
#     return d

# def div(x):
#     d = set()
#     for i in range(1, int(x ** 0.5) + 1):
#         if x % i == 0:
#             d.add(i)
#             d.add(x//i)
#     return sorted(d)

# for x in range(5_200_001, 6_000_000):
#     dp = fact(x)
#     d = div(x)
#     if len(dp) == 9 and len(d) % 90 == 0:
#         print(x, max(dp))

# 26683
# def fact(x):
#     d = []
#     i = 2
#     while i * i <= x:
#         while x % i == 0:
#             d.append(i)
#             x = x // i
#         i += 1
#     if x > 1:
#         d.append(x)
#     return d

# k = 0
# for x in range(8_000_010, 9_000_000, 100):
#     if k == 5: break
#     d = fact(x)
#     if len(d) == len(set(d)):
#         print(x, max(d))
#         k += 1

# 26686
# def fact(x):
#     d = []
#     i = 2
#     while i * i <= x:
#         while x % i == 0:
#             d.append(i)
#             x = x // i
#         i += 1
#     if x > 1:
#         d.append(x)
#     return d

# k = 0
# for x in range(89428305, 100_000_000):
#     if k == 6: break
#     d = fact(x)
#     if len(d) >= 6 and x % sum(d) == 0:
#         print(x, sum(d))
#         k += 1

# 27337
# def fact(x):
#     d = []
#     i = 2
#     while i * i <= x:
#         while x % i == 0:
#             d.append(i)
#             x = x // i
#         i += 1
#     if x > 1:
#         d.append(x)
#     return d

# k = 0
# for x in range(123_456_790, 200_000_000):
#     if k == 5: break
#     d = fact(x)
#     if len(d) == 7 and "5" in str(sum(d)) and max(d) % 10 == 9:
#         print(x, max(d))
#         k += 1

# 27338
# def fact(x):
#     d = []
#     i = 2
#     while i * i <= x:
#         while x % i == 0:
#             d.append(i)
#             x = x // i
#         i += 1
#     if x > 1:
#         d.append(x)
#     return d

# k = 0
# for x in range(987_654_321, 0, -1):
#     if k == 5: break
#     d = fact(x)
#     if len(d) == 13 and "1" in str(sum(d)):
#         print(x, max(d))
#         k += 1

# 26687
# def fact(x):
#     d = []
#     i = 2
#     while i * i <= x:
#         while x % i == 0:
#             d.append(i)
#             x = x // i
#         i += 1
#     if x > 1:
#         d.append(x)
#     return d

# k = 0
# for x in range(89_427_151, 100_000_000):
#     if k == 7: break
#     d = fact(x)
#     d2 = [c for c in d if d.count(c) == 2]
#     d1 = [c for c in d if d.count(c) == 1]
#     if len(d) == 8 and len(d2) == 4 and len(d1) == 4 and min(d) not in d2:
#         print(x, max(d))
#         k += 1

# 25129
# def div(x):
#     d = set()
#     for i in range(1, int(x ** 0.5) + 1):
#         if x % i == 0:
#             d.add(i)
#             d.add(x//i)
#     return sorted(d)

# for x in range(1_000_001, 2_000_000):
#     for n in range(0, 1000, 222):
#         if all(c not in str(n) for c in "02468"):
#             d = div(x - n)
#             if all(c == 5 for c in d):
#                 print(x, len(d))
# не работает

from math import *

# print(log(1000000, 5))
s = set()
for i in range(1, 13):
    s.add(5 ** i)
print(sorted(s))

k = 0
for x in range(1_000_001, 2_000_000):
    for i in s:
        if x > i:
            if (x - i) % 111 == 0 and k < 5 and (x - i) % 2 == 0 and all(c not in str(x-i) for c in "13579"):
                print(x, ceil(log(i, 5)))
                k+=1

# 25191
# from fnmatch import *

# a = []
# for x in range(10 ** 10):
#     if fnmatch(str(x), "88?0*0?6") and fnmatch(str(x), "88?03?056"):
#         a.append(x)
# print(max(a), min(a))
# print(max(a) % 62, min(a) % 62)
# не успел посчитаться