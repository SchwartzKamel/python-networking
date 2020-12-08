from __future__ import print_function


def get_ip():
    try:
        ip_address = raw_input("Enter an IP address: ")
        return ip_address
    except NameError:
        ip_address = input("Enter an IP address: ")
        return ip_address


ip_addr1 = get_ip()
ip_addr2 = get_ip()
ip_addr3 = get_ip()


print("First IP: " + ip_addr1,
      "\nSecond IP: " + ip_addr2,
      "\nThird IP: " + ip_addr3)
