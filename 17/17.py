# 25356
# a = [int(x) for x in open("17/17_25356.txt")]
# b = []
# c = []
# d = []

# for i in range(len(a)):
#     if 1000 <= abs(a[i]) <= 9999:
#         b.append(a[i])
#     if abs(a[i]) % 100 == 30:
#         c.append(a[i])
# for i in range(len(a) - 2):
#     if ((a[i] not in b) and (a[i + 1] not in b) and (a[i + 2] not in b)) and (a[i] + a[i + 1] + a[i + 2]) > max(c):
#         d.append(a[i] + a[i + 1] + a[i + 2])
# print(len(d), max(d))

# 25138313_17
# a = [int(x) for x in open("17/25138313_17.txt")]
# b = []
# c = []

# for i in range(len(a)):
#     if 10 <= abs(a[i]) <= 99:
#         b.append(a[i])
# for i in range(len(a)-1):
#     if ((a[i] in b) or (a[i+1] in b)) and (a[i] + a[i+1]) <= max(b):
#         c.append(a[i] + a[i+1])
# print(len(c), max(c))

# 24892
# a = [int(x) for x in open("17/17_24892.txt")]
# b = []
# c = []

# for i in range(len(a)):
#     if 1000 <= abs(a[i]) <= 9999 and a[i] < 0 and abs(a[i]) % 9 == 0:
#         b.append(a[i])
# for i in range(len(a)-1):
#     if ((a[i] < 0) + (a[i + 1] < 0)) == 1 and (a[i] + a[i+1]) > max(b):
#         c.append(a[i]**2 + a[i+1]**2)
# print(len(c), min(c))

# 23757
# a = [int(x) for x in open("17/17_23757.txt")]
# b = []
# c = []

# for i in range(len(a)):
#     if 10 <= a[i] <= 99:
#         b.append(a[i])
# for i in range(len(a)-1):
#     if ((a[i] in b) + (a[i+1] in b)) == 1 and (a[i] + a[i+1]) % min(b) == 0:
#         c.append(a[i] + a[i+1])
# print(len(c), max(c))

# 23276
# a = [int(x) for x in open("17/17_23276.txt")]
# b = []
# c = []
# d = []

# for i in range(len(a)):
#     if 1000 <= abs(a[i]) <= 9999:
#         b.append(a[i])
# for i in range(len(a)):
#     if abs(a[i]) % 100 == 25:
#         d.append(a[i])
# for i in range(len(a) - 2):
#     if ((a[i] in b) + (a[i+1] in b) + (a[i+2] in b)) <= 2 and (a[i] + a[i+1] + a[i+2]) <= max(d):
#         c.append(a[i] + a[i+1] + a[i+2])
# print(len(c), max(c))

# 22469
# a = [int(x) for x in open("17/17_22469.txt")]
# b = []
# c = []

# for i in range(len(a)):
#     if 10000 <= abs(a[i]) <= 99999 and abs(a[i]) % 2 != 0:
#         b.append(a[i])
# for i in range(len(a)-1):
#     if ((str(a[i])[-1:] == str(sum(b))[-1:]) + (str(a[i+1])[-1:] == str(sum(b))[-1:])) == 1:
#         c.append(a[i] * a[i+1])
# print(len(c), max(c))

# 21903
# a = [int(x) for x in open("17/17_21903.txt")]
# b = []
# c = []

# for i in range(len(a)):
#     if 100 <= abs(a[i]) <= 999 and str(a[i])[-2:] == "15":
#         b.append(a[i])
# for i in range(len(a)-2):
#     if ((a[i] > 0 and a[i+1] > 0 and a[i+2] > 0) or (a[i] < 0 and a[i+1] < 0 and a[i+2] < 0)) and min(a[i], a[i+1], a[i+2]) * max(a[i], a[i+1], a[i+2]) > min(b) ** 2:
#         c.append(min(a[i], a[i+1], a[i+2]) * max(a[i], a[i+1], a[i+2]))
# print(len(c), min(c))

# 21712
# a = [int(x) for x in open("17/17_21712.txt")]
# b = []
# c = []
# d = []

# for i in range(len(a)):
#     if 1000 <= abs(a[i]) <= 9999 and str(a[i])[-1] == "6":
#         b.append(a[i])
#         if a[i] > 0:
#             d.append(a[i])
# for i in range(len(a)-2):
#     if ((a[i] in b) + (a[i+1] in b) + (a[i+2] in b)) == 1 and (a[i] + a[i+1] + a[i+2]) <= min(d):
#         c.append(a[i] + a[i+1] + a[i+2])
# print(len(c), max(c))

# 21595
# a = [int(x) for x in open("17/17_21595.txt")]
# b = []
# c = []

# for i in range(len(a)):
#     if 1000 <= abs(a[i]) <= 9999 and str(a[i])[-1] == "3":
#         b.append(a[i])
# for i in range(len(a)-2):
#     sm = a[i] + a[i+1] + a[i+2]
#     if sm - min(a[i], a[i+1], a[i+2]) > len(b) ** 2:
#         c.append(sm)
# print(len(c), abs(max(c)))

# 21416
# a = [int(x) for x in open("17/17_21416.txt")]
# b = []
# c = []

# for i in range(len(a)):
#     if a[i] < 0:
#         b.append(a[i])
# for i in range(len(a)-2):
#     tr = [a[i], a[i+1], a[i+2]]
#     if min(tr) * max(tr) > sum(b):
#         c.append(sum(tr))
# print(len(c), abs(max(c)))

# 23904
# a = [int(x) for x in open("17/17_23904.txt")]
# k = 0
# n = 0

# for i in range(len(a) - 1):
#     if (a[i] % 5 == 0 and a[i] % 3 != 0) + (a[i+1] % 5 == 0 and a[i+1] % 3 != 0) == 1 and (a[i] % 9 == 0) + (a[i+1] % 9 == 0) != 1:
#         k += 1
#     if (a[i] % 9 == 0) + (a[i+1] % 9 == 0) == 1 and (a[i] % 5 == 0 and a[i] % 3 != 0) + (a[i+1] % 5 == 0 and a[i+1] % 3 != 0) != 1:
#         n += 1
# print(n + k, k - n)

# 19900
# a = [int(x) for x in open("17/17_19900.txt")]
# b = []
# c = []
# d = []

# for i in range(len(a)):
#     if 100 <= abs(i) <= 999:
#         b.append(i)
#     if 1000 <= abs(i) <= 9999:
#         c.append(i)
# for i in range(len(a) - 2):
#     if ((a[i] in b) + (a[i+1] in b) + (a[i+2] in b)) == 2 and a[i] * a[i+1] * a[i+2] > sum(c):
#         d.append(a[i] * a[i+1] * a[i+2])
# print(len(d), abs(min(d)))

# 18176
# a = [int(x) for x in open("17/17_18176.txt")]
# b = []
# c = []

# def sm(n):
#     return sum([int(x) for x in str(abs(n))])

# for i in range(len(a)):
#     if i > 0 and str(i)[-1] == "4":
#         b.append(i)
# for i in range(len(a) - 2):
#     if sm(a[i]) + sm(a[i+1]) + sm(a[i+2]) == min(b):
#         c.append(a[i] + a[i+1] + a[i+2])
# print(len(c), max(c))
def sum_dig(number):
    number = abs(number)
    sm = 0
    for x in str(number):
        sm += int(x)
    return sm

f = open("17/17_18176.txt")

min_4 = 10 ** 10
a = [int(x) for x in f]
for x in a:
    if str(x)[-1] == "4" and x > 0:
        min_4 = min(min_4, x)

count = 0
max_sum = -10 ** 10
for i in range(len(a) - 2):
    sm_dg1 = sum_dig(a[i])
    sm_dg2 = sum_dig(a[i+1])
    sm_dg3 = sum_dig(a[i+2])
    if sm_dg1 + sm_dg2 + sm_dg3 == min_4:
        count += 1
        max_sum = max(max_sum, a[i] + a[i+1] + a[i+2])
print(count, max_sum)