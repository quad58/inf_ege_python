#25360
# def f(x, y):
#     if x < y or x == 36:
#         return 0
#     if x == y:
#         return 1
#     if x > y:
#         return f(x-3, y) + f(x - 6, y) + f(x // 2, y)

# print(f(86, 53) * f(53, 12))

#26197
# def f(x, y):
#     if x > y:
#         return 0
#     if x == y:
#         return 1
#     if x < y:
#         return f(x+2, y) + f(x+3, y) + f(x*2, y)
    
# print(f(7, 21) * f(21, 32) + f(7, 14) * f(14, 32) - f(7, 14) * f(14, 21) * f(21, 32))

#24628
def f(x, y, k):
    if x > y or "6" in str(x) or k > 50:
        return 0
    if x == y:
        return 1
    if x < y:
        return f(x+1, y, k + 1) + f(x+5, y, k + 1) + f(x*2, y, k + 1)
    
print(f(0, 312025, 0))