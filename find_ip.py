from utils import *

if __name__ == "__main__":
    interface = get_interface()
    ip = get_host_ip(interface)
    netmask, mask_length = get_host_submask(interface)
    subnet = get_subnet(ip, netmask)
    ping_text = ping(subnet, mask_length)
    ip_lives = get_ip_lives(ping_text)
    mac_list = get_mac_list(ip_lives)
    ip_target = check_mac(zip(ip_lives, mac_list))
    write_history(ip_target)


