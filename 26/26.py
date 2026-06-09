#k 2617
# f = open("26/2617.txt")
# S, N = [int(x) for x in f.readline().split()]
# a = [int(x) for x in f]
# a.sort()
# b = []
# for x in a:
#     if sum(b) + x <= S:
#         b.append(x)
# print(len(b))
# b.pop(-1)
# print(max(x for x in a if sum(b) + x <= S))

#k 4102
# f = open("26/26-55.txt")
# N, S = [int(x) for x in f.readline().split()]
# a = [int(x) for x in f]
# a.sort(reverse=1)
# b = []
# while len(a) > 0:
#     ship = []
#     for i in range(len(a)):
#         if sum(ship) + a[i] <= S:
#             ship.append(a[i])
#             a[i] = 0
#     a = [x for x in a if x != 0]
#     b.append(sum(ship))
# print(len(b), b[-1])

#k 5037
# f = open("26/26-79.txt")
# N, K = [int(x) for x in f.readline().split()]
# a = []
# for s in f:
#     r, m = [int(x) for x in s.split()]
#     a.append([r, m])
#     a.sort()
# for d1, d2 in zip(a, a[1:]):
#     r1, m1 = d1
#     r2, m2 = d2
#     if r1 == r2 and m2 - m1 == K + 1:
#         print(r1, m1 + 1)

#k 7943
# f = open("26/26-159.txt")
# N = int(f.readline())
# a = []
# for s in f:
#     st, z = [int(x) for x in s.split()]
#     a.append((st, z))
# a = sorted(set(a))
# k = 1
# m = []
# for x, y in zip(a, a[1:]):
#     st1, z1 = x
#     st2, z2 = y
#     if st1 == st2 and z2 - z1 == 1:
#         k += 1
#         if k == 148:
#             print(st1)
#         m.append(k)
#     else:
#         k = 1
# print(max(m))

#k 5232
# f = open("26/26-82.txt")
# N = int(f.readline())
# a = []
# for s in f:
#     x, y = [int(x) for x in s.split()]
#     if y % 2 != 0:
#         a.append((x, y))
# a = sorted(set(a))
# k = 1
# m = []
# for z, w in zip(a, a[1:]):
#     x1, y1 = z
#     x2, y2 = w
#     if x1 == x2:
#         k += 1
#         if k == 17:
#             print(x1)
#         m.append(k)
#     else:
#         k = 1
# print(max(m))

#k 5325
# f = open("26/26-89.txt")
# N = int(f.readline())
# a = [int(x) for x in f]
# a.sort(reverse=1)
# b = [a[0]]
# for x in a[1:]:
#     if b[-1] - x >= 3:
#         b.append(x)
# print(len(b), b[-1])

#k 6092
# f = open("26/26-101.txt")
# N, K = [int(x) for x in f.readline().split()]
# a = [int(x) for x in f]
# a.sort(reverse=1)
# b = []
# while len(a) > 0:
#     box = [a[0]]
#     for i in a:
#         if box[-1] - i >= K:
#             box.append(i)
#     for x in box:
#         a.remove(x)
#     b.append(len(box))
# print(len(b), max(b))

#k 6790
# f = open("26/26-128.txt")
# N = int(f.readline())
# a = []
# for s in f:
#     st, end = [int(x) for x in s.split()]
#     a.append([st, end])
# a = sorted(a, key=lambda x: (x[1], x[0]))
# b = [a[0]]
# for x in a[1:]:
#     stp, endp = b[-1]
#     st, end = x
#     if st >= endp:
#         b.append(x)
# print(len(b))
# b.pop(-1)
# print([x for x in a if x[0] >= b[-1][1]])

#k 6791
# f = open("26/26-129.txt")
# N = int(f.readline())
# a = []
# k = 0
# for s in f:
#     k += 1
#     sh, ok = [int(x) for x in s.split()]
#     if sh < ok:
#         a.append([sh, "sh", k])
#     else:
#         a.append([ok, "ok", k])
# a.sort()
# print(a[-1])
# print(len([x for x in a if x[1] == "sh"])-1)

#k 7506
# f = open("26/26-151.txt")
# N, S = [int(x) for x in f.readline().split()]
# a = []
# for s in f:
#     ID, b1, b2, b3, so = [int(x) for x in s.split()]
#     a.append([ID, b1 + b2 + b3, so])

# a.sort(key = lambda x: (x[1], x[2], -x[0]), reverse=1)
# print(a[S - 1])
# print(a[S - 50: S + 50])
# print(len([x for x in a if x[1] == 154]))

#k 7620
# f = open("26/26-154.txt")
# N = int(f.readline())
# a = []
# b = []
# for s in f:
#     ID, b1, b2, b3, b4 = [int(x) for x in s.split()]
#     if 2 not in [b1, b2, b3, b4]:
#         a.append([ID, sum([b1, b2, b3, b4]) / 4])
#     else:
#         b.append([ID, len([x for x in [b1, b2, b3, b4] if x == 2])])
# a.sort(key = lambda x: (x[1], -x[0]), reverse=1)
# b.sort(key = lambda x: (x[1], x[0]))
# print(a[N // 4 - 1])
# print([x for x in b if x[1] > 2][0])

#k 4933
# f = open("26/26-75.txt")
# N = int(f.readline())
# timeline = [0] * 1000000
# for s in f:
#     start, end = [int(x) for x in s.split()]
#     for i in range(start, end):
#         timeline[i] += 1
# print(max(timeline))
# print(len([x for x in timeline if x != 0]))

#k 7109
# f = open("26/26-140.txt")
# N = int(f.readline())
# timeline = [" "] * 44640
# for s in f:
#     start, end = [int(x) for x in s.split()]
#     for i in range(start, end):
#         timeline[i] = "1"
# print(timeline.count("1"), max([len(c) for c in ''.join(timeline).split()]))

#k 6316
# f = open("26/26-111.txt")
# K = int(f.readline())
# N = int(f.readline())
# a = []
# for s in f:
#     start, end = [int(x) for x in s.split()]
#     a.append([start, end])
# a.sort()
# kamera = [0] * K
# r = []
# for start, end in a:
#     for i in range(K):
#         if kamera[i] < start:
#             kamera[i] = end
#             r.append(i + 1)
#             break
# print(len(r), r[-1])

#k 6406
f = open("26/26-119.txt")
N, L, M = [int(x) for x in f.readline().split()]
a = []
for s in f:
    st, d, t = s.split()
    st, d = int(st), int(d)
    a.append([st, d, t])
a.sort()
l = [0] * L
m = [0] * M
kl = 0
km = 0
for st, d, t in a:
    if t == "A":
        for i in range(L):
            if l[i] <= st:
                l[i] = st+d
                kl += 1
                break
        else:
            for i in range(M):
                if m[i] <= st:
                    m[i] = st + d
                    kl += 1
                    break
    if t == "B":
        for i in range(M):
            if m[i] <= st:
                m[i] = st+d
                km += 1
                break
print(km, N - kl - km)