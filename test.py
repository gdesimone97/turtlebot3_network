from utils import get_host_submask

# a = get_addresses("192.168.1.1")
b = bin(255)
c = b.count("1")

a, b = get_host_submask("wlp0s20f3")
pass