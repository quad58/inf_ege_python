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
from fnmatch import *

def p(x):
    return x > 1 and all(x % i != 0 for i in range(2, int(x ** 0.5) + 1))

for x in range(0, 10 ** 7):
    if fnmatch(str(x), "31*567?") and p(x) == 1:
        s = 1
        for c in str(x):
            s *= int(c)
        print(x, s)