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
s = open("24/24-310.txt").readline()
reg = r"([1-2][0-2]*|0)"
reg = rf"{reg}([*+]{reg})*"
m = max([x.group() for x in finditer(reg, s)], key=len)
print(len(m), m)