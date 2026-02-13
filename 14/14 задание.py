#25353
# for x in range(1, 27001):
#     a = 3 * 27 ** 9 + 2 * 27 ** 6 + 27 ** 3 - x
#     k = 0
#     while a > 0:
#         if a % 27 == 0:
#             k += 1
#         a = a // 27
#     if k == 6:
#         print(x)
#         break

# 24890
# for x in range(1, 7291):
#     a = 27 ** 298 + 27 ** 269 - x
#     k = 0
#     s = []
#     while a > 0:
#         if a % 27 == 0:
#             k += 1
#         a = a // 27
#     s.append(k)
# print(max(s))

# 20960
# m = 0
# mx = 0
# for x in range(1, 2006):
#     a = 5 ** 150 + 5 ** 98 - x
#     k = 0
#     while a > 0:
#         if a % 5 == 0:
#             k += 1
#         a = a // 5
#     if m < k:
#         m = k
#         mx = x
# print(m, mx)

# 20904
# for x in range(1, 2031):
#     a = 3 ** 100 - x
#     k = 0
#     while a > 0:
#         if a % 3 == 0:
#             k += 1
#         a = a // 3
#     if k == 1:
#         print(x)

# 19484
# a = 5 * 729 ** 2024 + 3 * 243 ** 1413 - 7 * 81 ** 169 - 2 * 9 ** 107 + 3017
# k = 0
# while a > 0:
#     if a % 27 % 2 == 0 and a % 27 <= 25:
#         k += a % 27
#     a = a // 27
# print(k)

# 19246
# abcdefghijklmnopqrstuvwxyz
# for x in "0123456789abcdefghijklmno":
#     a1 = int(f"11353{x}12", 25)
#     a2 = int(f"135{x}21", 25)
#     r = a1 + a2
#     if r % 24 == 0:
#         print(r / 24)

# 23373
# a = 2 * 2401 ** 525 + 3 * 343 ** 524 - 4 * 49 ** 523 + 5 * 49 ** 522 - 6 * 7 ** 521 - 35
# k = 0
# while a > 0:
#     if a % 49 <= 9:
#         k += 1
#     a = a // 49
# print(k)

# 19406
# from string import *
# for x in printable[:35]:
#     a1 = f"6{x}qr{x}"
#     a2 = f"{x}59sh"
#     a3 = f"ph{x}69yw"
#     a = int(a1, 35) + int(a2, 35) + int(a3, 35)

#     maxxl = []
#     maxx = -1
#     maxc = 0

#     for x1 in str(a):
#         if maxc < str(a).count(x1):
#             maxxl.append(int(x1))
#             if maxx != -1:
#                 maxxl.remove(maxx)
#             maxx = int(x1)
#             maxc = str(a).count(x1)

#     maxx = max(maxxl)
#     # print(a, maxxl, maxx)
#     if a % maxx ** 2 == 0:
#         print(x, a, maxx, a//(maxx ** 2))

#     # b = 10 * [0]
#     # for x in str(a):
#     #     for i in len(b):
#     #         if int(x) == i:
#     #             b[i] += 1

# 7346
# for x in range(67):
#     a = 3 * 81 ** 3 + x * 81 ** 2 + 2 * 81 + 1
#     b = 1 * 67 ** 3 + 7 * 67 ** 2 + x * 67 + 4
#     r = a + b
#     if r % 35 == 0:
#         print(r//35)

# 6846
# for x in range(98):
#     a = 1 * 98 ** 4 + 2 * 98 ** 3 + x * 98 ** 2 + 4 * 98 + 5
#     b = 1 * 123 ** 3 + x * 123 ** 2 + 9 * 123 + 8
#     r = a + b
#     if r % 123 == 0:
#         print(r//123)

# 24739
from string import *
for x in printable[:21]:
    a1 = f"ef{x}67"
    a2 = f"3h{x}4c"
    r = int(a1, 21) + int(a2, 21)
    if r % 20 == 0:
        print(r//7)