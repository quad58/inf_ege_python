from re import *

#k 2510
# s = open("24/k7a-1.txt").readline()
# reg = r"[ABC]+"
# print(max([len(x.group()) for x in finditer(reg, s)]))

#k 4923
# s = open("24/24-196.txt").readline()
# reg = r"(ZX|ZY)+"
# print(max([len(x.group())//2 for x in finditer(reg, s)]))

#k 5327
# s = open("24/24-212.txt").readline()
# reg = r"([BCD][AO])+"
# print(max([len(x.group())//2 for x in finditer(reg, s)]))

#k 5155
# s = open("24/24-204.txt").readline()
# reg = r"(AA|CC)+"
# reg = rf"(?=({reg}))"
# print(max([len(x.group(1))//2 for x in finditer(reg, s)]))

#k 5391
# s = open("24/24-215.txt").readline()
# reg = r"([123][ABC][123])+"
# reg = rf"(?=({reg}))"
# print(max([len(x.group(1))//3 for x in finditer(reg, s)]))

#k 5936
# s = open("24/24-239.txt").readline()
# reg = r"(YZZ|XY|YZ)+"
# reg = rf"(?=({reg}))"
# print(max([len(x.group(1)) for x in finditer(reg, s)]))

#k 7497
# s = open("24/24-298.txt").readline()
# reg = r"([1-9][0-9]*)"
# reg = rf"{reg}([*-]{reg})*"
# m = max([x.group() for x in finditer(reg, s)], key=len)
# print(len(m), m)

#k 7966
# s = open("24/24-310.txt").readline()
# reg = r"([1-2][0-2]*|0)"
# reg = rf"{reg}([*+]{reg})*"
# m = max([x.group() for x in finditer(reg, s)], key=len)
# print(len(m), m)

#k 7573
# s = open("24/24-299.txt").readline()
# reg = r"([1-9][0-9]*|0)"
# reg = rf"(({reg}\*)*0(\*{reg})*)"
# reg = rf"{reg}(\+{reg})*"
# m = max([x.group() for x in finditer(reg, s)], key=len)
# print(len(m), m)

#k 7786
# s = open("24/24-305.txt").readline()
# reg = r"([1-9][0-9]*|0)"
# reg = rf"AF{reg}([+*]{reg})*"
# m = max([x.group() for x in finditer(reg, s)], key=len)
# print(len(m), m)

# 23568
# s = open("24/24_23568.txt").readline()
# reg = r"(?=([A-Z][0-9]+[A-Z]))"
# a = []
# for x in finditer(reg, s):
#     c = x.group(1)
#     if c[0] == c[-1]:
#         a.append(len(c))
#     if len(c) == 1952:
#         print(s.find(c))
# # print(max(a))

# 23424
# s = open("24/24 (5)_23424.txt").readline()
# reg = r"(?=([AEIOUY][0-9]+[AEIOUY]))"
# a = []
# for x in finditer(reg, s):
#     c = x.group(1)
#     if c[0] == c[-1]:
#         a.append(len(c))
# print(max(a))

# 20968
# s = open("24/24_20968.txt").readline()
# reg = r"([1-9][0-9]*[02468]|[02468])"
# reg = rf"{reg}([+*]{reg})*"
# m = max([x.group() for x in finditer(reg, s)], key=len)
# print(len(m), m)

# 22356
# s = open("24/24_22356.txt").readline()
# reg = r"[1-9AB][0-9AB]+[13579B]"
# m = max([x.group() for x in finditer(reg, s)], key=lambda x:int(x, 12))
# print(s.find(m))

# 22357
# s = open("24/24_22357.txt").readline()
# reg = r"[1-9A-D][0-9A-D]+[02468AC]"
# m = max([x.group() for x in finditer(reg, s)], key=lambda x:int(x, 14))
# print(s.find(m))

# 22358
# s = open("24/24_22358.txt").readline()
# reg = r"[1-9AB][0-9AB]+[0369]"
# m = max([x.group() for x in finditer(reg, s)], key=lambda x:int(x, 12))
# print(s.find(m))

# 21597
# s = open("24/24_21597.txt").readline()
# reg = r"[1-5][0-5]*|0"
# reg = rf"{reg}(\*{reg})*(-{reg})*"
# reg = rf"(?=({reg}))"
# m = max([x.group(1) for x in finditer(reg, s)], key=len)
# print(len(m), m)

### ДВОЙНОЙ ЦИКЛ №1 ###
# s = open("24/k7a-3.txt").readline()

# m = 0

# for l in range(len(s)):
#     for r in range(l+m, len(s) + 1):
#         c = s[l:r]
#         if "C" in c or "D" in c: break
#         m = max(m, len(c))
# print(m)

#k 4217
# s = open("24/24-157.txt").readline()

# m = 0

# for l in range(len(s)):
#     for r in range(l+m, len(s) + 1):
#         c = s[l:r]
#         if "QW" in c: break
#         m = max(m, len(c))
# print(m)

#k 7941
# s = open("24/24-309.txt").readline()

# m = 0

# for l in range(len(s)):
#     for r in range(l+m, len(s) + 1):
#         c = s[l:r]
#         if c.count("FSRQ") > 80: break
#         if c.count("FSRQ") == 80: m = max(m, len(c))
# print(m)

#k 6675
# s = open("24/24-263.txt").readline()

# m = 0

# for l in range(len(s)):
#     for r in range(l+m, len(s) + 1):
#         c = s[l:r]
#         if c.count("Y") > 150: break
#         m = max(m, len(c))
# print(m)

# 17535
# s = open("24/24_17535.txt").readline()

# m = 0

# for l in range(len(s)):
#     for r in range(l + m, len(s) + 1):
#         c = s[l:r]
#         if c.count("CD") > 160: break
#         if c.count("CD") == 160: m = max(m, len(c))
# print(m)

#k 6674
# s = open("24/24-263.txt").readline()

# m = 10 ** 5

# for l in range(len(s)):
#     for r in range(l+m, l, -1):
#         c = s[l:r]
#         if c.count("Z") < 120: break
#         m = min(m, len(c))
# print(m)

#k 8834
# s = open("24/24-371.txt").readline()

# m = 10000

# for l in range(len(s)):
#     for r in range(l+m, l, -1):
#         c = s[l:r]
#         if c.count(".") == 0 and c.count("A") < 98: break
#         if c.count(".") == 1 and c[-1] == "." and c.count("A") == 98: m = min(m, len(c))
# print(m)

#k 8695
# s = open("24/24-361.txt").readline()

# m = 0

# for l in range(len(s)):
#     for r in range(l+m, len(s) + 1):
#         c = s[l:r]
#         # if c.count("2025") < 90: break
#         if c.count("Y") > 80: break
#         if c.count("2025") >= 90 and c.count("Y") == 80: m = max(m, len(c))
# print(m)

# 26077
# s = open("24/24_26077.txt").readline()

# m = 0

# for l in range(len(s)):
#     for r in range(l+m + 1, len(s) + 1):
#         c = s[l:r]
#         for j in "13579":
#             c = c.replace(j, "1")
#         if c[0]!='G' or c.count('1')>45 or c.count('G')>1: break
#         if c.count("1") == 45: m = max(m, len(c))
# print(m)

# 23568
# s = open("24/24_23568.txt").readline()

# reg = r"(?=([A-Z][0-9]+[A-Z]))"
# a = []
# for x in finditer(reg, s):
#     c = x.group(1)
#     if c[0] == c[-1]:
#         a.append(len(c))
#         if len(c) == 1952:
#             print(s.find(c))
# print(max(a))

# 28765
s = open("24/24_28765.txt").readline()

m = 1

for l in range(len(s)):
    for r in range(l+m, len(s)+1):
        c = s[l:r]
        if c.count("BC") > 180: break
        m = max(m, len(c))
    if l%100_000==0: print(l,len(s),m)

print(m)