# 25138313_17
# def f(a, b, m):
#     if a + b >= 255: return m % 2 == 0
#     if m == 0: return 0
#     h = [f(a+1, b, m-1), f(a, b+1, m-1), f(a*2, b, m-1), f(a, b*2, m-1)]
#     return any(h) if (m-1) % 2 == 0 else all(h)
# print(19, [s for s in range(1, 234) if f(21, s, 2)])
# print(20, [s for s in range(1, 234) if not f(21, s, 1) and f(21, s, 3)])
# print(21, [s for s in range(1, 234) if not f(21, s, 2) and f(21, s, 4)])

# 25358
# def f(s, m):
#     if s >= 125:
#         return m % 2 == 0
#     if m == 0:
#         return 0
#     h = [f(s+2, m-1), f(s+4, m-1), f(s*2, m-1)]
#     return any(h) if (m-1)%2 == 0 else all(h)
# print(19, [s for s in range(1, 125) if f(s, 2)])
# print(20, [s for s in range(1, 125) if (not f(s, 1)) and f(s, 3)])
# print(21, [s for s in range(1, 125) if (not f(s, 2)) and f(s, 4)])

# 22066
# def f(a, b, m):
#     if a + b >= 100: return m%2 == 0
#     if m == 0: return 0
#     h = [f(a+3, b, m-1), f(a, b+3, m-1), f(a*2, b, m-1), f(a, b*2, m-1)]
#     return any(h) if (m-1)%2 == 0 else all(h)
# print(19, [s for s in range(1, 83) if f(17, s, 2)])
# print(20, [s for s in range(1, 83) if (not f(17, s, 1)) and f(17, s, 3)])
# print(21, [s for s in range(1, 83) if (not f(17, s, 2)) and f(17, s, 4)])

#20825
# def f(a, b, m):
#     if a + b <= 69: return m%2 == 0
#     if m == 0: return 0
#     h = [f(a//2, b, m-1), f(a, b//2, m-1), f(a-5, b+2, m-1), f(a+2, b-5, m-1)]
#     return any(h) if (m-1)%2 == 0 else all(h)
# print(19, [s for s in range(51, 1000) if f(35, s, 2)])
# print(20, [s for s in range(51, 1000) if (not f(35, s, 1)) and f(35, s, 3)])
# print(21, [s for s in range(51, 1000) if (not f(35, s, 2)) and f(35, s, 4)])

#22438
# from math import *
# def f(s, m):
#     if s <= 23: return m%2 == 0
#     if m == 0: return 0
#     h = [f(s-3, m-1), f(s-5, m-1), f(s-3, m-1), f(ceil(s/2), m-1)]
#     return any(h) if (m-1)%2 == 0 else all(h)
# print(19, [s for s in range(24, 1000) if f(s, 2)])
# print(20, [s for s in range(24, 1000) if (not f(s, 1)) and f(s, 3)])
# print(21, [s for s in range(24, 1000) if (not f(s, 2)) and f(s, 4)])

# 13965
# def f(a, b, m):
#     if a * b >= 541: return m%2 == 0
#     if m == 0: return 0
#     h = [f(a + 10, b, m - 1), f(a, b + 10, m - 1), f(a * 2, b, m - 1), f(a, b * 2, m - 1)]
#     return any(h) if (m-1)%2 == 0 else all(h)
# print(19, [s for s in range(1, 91) if f(6, s, 2)])
# print(20, [s for s in range(1, 91) if (not f(6, s, 1)) and f(6, s, 3)])
# print(20, [s for s in range(1, 91) if (not f(6, s, 2)) and f(6, s, 4)])

# 23329
# from math import *
# def f(a, b, m):
#     if a + b <= 60: return m%2 == 0
#     if m == 0: return 0
#     h = [f(a-5, b, m-1), f(a, b-3, m-1), f(a//2, b, m-1), f(a, ceil(b/2), m-1)]
#     return any(h) if (m-1)%2 == 0 else all(h)
# print(19, [s for s in range(5, 151) if f(130, s, 2)])
# print(20, [s for s in range(5, 151) if (not f(130, s, 1)) and f(130, s, 3)])
# print(21, [s for s in range(5, 151) if (not f(130, s, 1)) and(not f(130, s, 3)) and f(130, s, 5)]) # 162020880

# 12737
def f(a, b, m):
    if a * b > 384: return m%2 == 0
    if m == 0: return 0
    h = [f(a+5, b, m-1), f(a, b+5, m-1), f(a*2, b, m-1), f(a, b*2, m-1)]
    return any(h) if (m-1)%2 == 0 else all(h)
print(19, [s for s in range(1, 55) if f(8, s, 2)])
print(20, [s for s in range(1, 55) if (not f(8, s, 1)) and f(8, s, 3)])
print(21, [s for s in range(1, 55) if (not f(8, s, 2)) and f(8, s, 4)])