# 25347
# from itertools import *

# i = 1
# for s in product(sorted("ГРАНИТ"), repeat=6):
#     if i % 2 != 0 and s[0] != "А" and s[0] != "И" and s[0] != "Г" and s.count("А") == 1:
#         print(i, s)
#         break
#     i += 1

# 24984
# from itertools import *

# k = 0
# for s in product("0123456789ABCDEF", repeat=5):
#     if s[0] != "0" and all(s.count(c) <= 2 for c in "0123456789ABCDEF") and any(c in s for c in "149"):
#         k += 1
# print(k)

# 25682
from itertools import *
i = 1
for s in product(sorted("ЩЁЛОЧЬ"), repeat=6):
    s = ''.join(s)
    if "Ь" in s and s[0] != "Ь":
        s = s.replace("Щ", "*").replace("Л", "*").replace("Ч", "*")
        if s.count("*") <= 2:
            print(i)
    i += 1