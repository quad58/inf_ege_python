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
s = open("24/24_21597.txt").readline()
reg = r"[1-5][0-5]*|0"
reg = rf"{reg}(\*{reg})*(-{reg})*"
reg = rf"(?=({reg}))"
m = max([x.group(1) for x in finditer(reg, s)], key=len)
print(len(m), m)