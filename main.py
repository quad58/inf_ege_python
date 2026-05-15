import random
from string import *

s = ""
for i in range(32):
    s += random.choice("0123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM%-_+")
print(s)