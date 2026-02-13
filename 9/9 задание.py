
# 25348
# f = open("9/9_25348.csv")

# k = 0
# for s in f:
#     a = [int(x) for x in s.split(";")]
#     a3 = [x for x in a if a.count(x) == 3]
#     a1 = [x for x in a if a.count(x) == 1]
#     if len(a3) == 3 and len(a1) == 4 and max(a) not in a3:
#         k += 1
# print(k)

# 23747
# f = open("9/9_23747.txt")

# for s in f:
#     a = [int(x) for x in s.split()]
#     a3 = [x for x in a if a.count(x) == 3]
#     a1 = [x for x in a if a.count(x) == 1]
#     if len(a3) == 3 and len(a1) == 4 and sum(a1) / 4 <= a3[0]:
#         print(sum(a))

# 23555
# f = open("9/9_23555.txt")

# k = 0
# for s in f:
#     a = [int(x) for x in s.split()]
#     a3 = [x for x in a if a.count(x) == 3]
#     a2 = [x for x in a if a.count(x) == 2]
#     a1 = [x for x in a if a.count(x) == 1]
#     if len(a3) == 3 and len(a2) == 2 and len(a1) == 2 and max(a3 + a2) > max(a1):
#         k += 1
# print(k)

# 23368
# f = open("9/9_23368.txt")

# n = 0
# for s in f:
#     a = [int(x) for x in s.split()]
#     a1 = [x for x in a if a.count(x) == 1]
#     a = sorted(a)
#     n += 1
#     if len(a) == len(a1) and (max(a) + min(a)) * 2 == 3 * (a[1] + a[2] + a[3]):
#         print(n)

# 22547
# f = open("9/9_22547.txt")

# for s in f:
#     a = [int(x) for x in s.split()]
#     a1 = [x for x in a if a.count(x) == 1]
#     a_s = sorted(a)
#     a_ch = [x for x in a if x % 2 == 0]
#     a_nc = [x for x in a if x % 2 != 0]
#     if len(a) == len(a1) and a_s == a and len(a_ch) == len(a_nc):
#         print(sum(a))

# 21976
# f = open("9/9_21976.txt")

# for s in f:
#     a = [int(x) for x in s.split()]
#     a1 = [x for x in a if a.count(x) == 1]
#     a_ch = [x for x in a if x % 2 == 0]
#     a_nc = [x for x in a if x % 2 != 0]
#     if len(a) == len(a1) and sum(a_ch) ** 2 > sum(a_nc) ** 3:
#         print(sum(a))

# 21704
# f = open("9/9_21704.txt")

# for s in f:
#     a = [int(x) for x in s.split()]
#     a_s = sorted(a)[::-1]
#     if a == a_s and (a[0] + a[6]) / 2 > (a[1] + a[2] + a[3] + a[4] + a[5]) / 5:
#         print(sum(a))
#         break

# 21592
# f = open("9/9_21592.txt")

# n = 0
# for s in f:
#     a = [int(x) for x in s.split()]
#     a2 = [x for x in a if a.count(x) == 2]
#     a1 = [x for x in a if a.count(x) == 1]
#     a1_k = [x ** 2 for x in a1]
#     n += 1
#     if len(a2) == 6 and len(a1) == 2 and (max(a2) - min(a2)) ** 2 > sum(a1_k) * 2:
#         print(n)

# 20899
# f = open("9/9_20899.txt")

# k = 0
# for s in f:
#     a = [int(x) for x in s.split()]
#     a2 = [x for x in a if a.count(x) == 2]
#     if max(a) < sum(a) - max(a) and len(a2) == 2:
#         k += 1
# print(k)

# 20488
f = open("9/9_20488.txt")

k = 0
for s in f:
    a = [int(x) for x in s.split()]
    a_p = [x for x in a if a.count(x) > 1]
    a_np = [x for x in a if a.count(x) == 1]
    if len(a_p) > 1 and len(a_np) > 1 and max(a) not in a_p and sum(a_np) / sum(a_p) >= 3:
        k += 1
print(k)