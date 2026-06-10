from ipaddress import *

k = 0
net = ip_network("103.161.48.0/255.255.240.0", 0)
for ip in net:
    s = bin(int(ip))[2:]
    if s.count("1") % 2 == 0:
        k += 1
print(k)