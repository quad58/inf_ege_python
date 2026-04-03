# 25352
from ipaddress import *

# net = ip_network("190.202.83.62/255.255.252.0", 0)
# print(net)
# print(190 + 202 + 83 + 254)

# 10572
# from ipaddress import *

# for mask in range(33):
#     net = ip_network(f"173.103.25.118/{mask}", 0)
#     print(net, 32 - mask)

# 10574
# for mask in range(33):
#     net = ip_network(f"158.116.11.146/{mask}", 0)
#     print(net)

# 10578
# for mask in range(33):
#     net1 = ip_network(f"10.96.180.231/{mask}", 0)
#     net2 = ip_network(f"10.96.140.118/{mask}", 0)
#     if net1 != net2:
#         print(32 - mask)

#10569
# net = ip_network("10.8.248.131/255.255.224.0", 0)
# print(net)

# # 10580
# net = ip_network(f"10.48.96.0/255.255.240.0", 0)
# k = 0
# for ip in net:
#     b = f'{ip:b}'
#     if b.count("1") > b.count("0"):
#         k += 1
# print(k)

# 10579
# net = ip_network("192.168.240.0/255.255.255.0")
# k = 0
# for ip in net:
#     b = f"{ip:b}"
#     if b.count("1") == b.count("0"):
#         k += 1
# print(k)

# 13828
# net = ip_network("192.168.32.48/255.255.255.192", 0)
# k = 0
# for ip in net:
#     b = f"{ip:b}"
#     if b.count("1") % 5 != 0:
#         k += 1
# print(k)

# 10575
# for mask in range(33):
#     net = ip_network(f"118.193.30.139/{mask}", 0)
#     print(net, net.netmask)

# 10167
# for mask in range(33):
#     net = ip_network(f"108.133.75.91/{mask}", 0)
#     print(net, net.num_addresses)

# 10151
# for mask in range(33):
#     net = ip_network(f"111.81.208.27/{mask}", 0)
#     print(net, net.netmask)

# 17767
# net = ip_network("228.172.236.0/255.255.240.0", 0)
# k = 0
# for ip in net:
#     b = f"{ip:b}"
#     if b.count("1") % 5 != 0:
#         k += 1
# print(k)

# 23751
# net = ip_network("191.128.66.83/255.192.0.0", 0)
# print(net[-1])

# 20902
# net = ip_network("172.16.80.0/255.255.248.0", 0)
# k = 0
# for ip in net:
#     b = f'{ip:b}'
#     if b.count("1") % 2 != 0:
#         k += 1
# print(k)

# 21745
# for mask in range(33):
#     net1 = ip_network(f"95.24.2.9/{mask}", 0)
#     net2 = ip_network(f"95.24.3.10/{mask}", 0)
#     if net1.network_address != net2.network_address:
#         print(sum(1 for ip in net1.hosts() if f'{ip:b}'[-1] == '0'))
#         print(sum(1 for ip in net2.hosts() if f'{ip:b}'[-1] == '0'))

# 23856
# net = ip_network("172.95.116.174/255.255.192.0", 0)
# for ip in net:
#     b = f"{ip:b}"
#     if b.count("1") % 5 == 0:
#         print(ip)
#         break
# print(172+95+64+15)

# 23857
# net = ip_network("192.168.12.207/255.192.0.0", 0)
# for ip in net:
#     b = f"{ip:b}"
#     if b.count("1") == b.count("0"):
#         print(ip)

# 22466
# net = ip_network("98.71.254.171/255.248.0.0", 0)
# for ip in net:
#     b = f"{ip:b}"
#     if b.count("1") % 7 == 0:
#         print(ip)
#         break

# 25798
# for mask in range(33):
#     net = ip_network(f"212.154.18.25/{mask}", 0)
#     print(net)

# print(bin(992))

# 25708
# for mask in range(33):
#     net = ip_network(f"212.154.18.25/{mask}", 0)
#     print(net)
# print(2 ** 9 - 2)

# 25138313_6
# ip = ip_address("212.154.18.25")
# ip = int(ip)
# ip = bin(ip)[2:]
# print(ip)
# 11010100100110100001001000011001
# k = 0
# net = ip_network("212.170.120.144/255.255.255.240", 0)
# for ip in net:
#     ip = int(ip)
#     ip = bin(ip)[2:]
#     if ip.count("1") > ip.count("0"):
#         k += 1
# print(k)

# 23857
# net = ip_network("192.168.12.207/255.192.0.0", 0)
# for ip in net:
#     s = f"{int(ip):032b}"
#     if s.count("1") == s.count("0"):
#         print(ip)

# 23855
# net = ip_network("172.95.116.174/255.255.192.0", 0)
# print(net[1])

# 17554
# k = 0
# net = ip_network("112.160.0.0/255.240.0.0", 0)
# for ip in net:
#     s = f"{int(ip):032b}"
#     if s.count("1") % 3 != 0:
#         k += 1
# print(k)

# 14648
# for mask in range(24):
#     net = ip_network(f"218.48.192.56/{mask}", 0)
#     print(net)

# 12947
# k = 0
# net = ip_network("203.111.195.0/255.255.240.0", 0)
# for ip in net:
#     s = f"{int(ip):032b}"
#     if (32 - s.count("1")) % 3 == 0 and "111" in s and "000" in s:
#         k += 1
# print(k)

# 11782
# a = []
# net = ip_network("129.128.0.0/255.128.0.0", 0)
# for ip in net:
#     s = f"{int(ip):032b}"
#     a.append(s.count("0"))
# print(min(a))

# 11774
# k = 0
# net = ip_network("214.96.0.0/255.240.0.0", 0)
# for ip in net:
#     s = f"{int(ip):032b}"
#     if s.count("0") % 3 == 0:
#         k += 1
# print(k)

#k 8915
# for mask in range(33):
#     net = ip_network(f"195.154.162.96/{mask}", 0)
#     print(net)

#k 8790
# net = ip_network("70.220.85.104/255.255.248.0", 0)
# print(net[-1])
# print(70+220+87+255)

#k 8616
# net = ip_network("208.192.226.58/255.240.0.0", 0)
# # for ip in net:
# #     a = int(ip)
# #     s = bin(a)[2:]
# #     if s.count("1") % 5 == 0 and ip != net[-1]:
# #         print(ip)
# print(208+207+255+224)

#k 8612
# net = ip_network("198.89.213.75/255.255.254.0", 0)
# print(net[1])
# print(198+89+212+1)

#k 8609
net = ip_network("191.128.66.83/255.192.0.0", 0)
print(net[-2])