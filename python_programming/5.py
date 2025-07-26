#Write a loop that pings a list of IPs (use os.system("ping")) 3
import os
import ipaddress
IPs=('192.168.56.1','8.8.8.8','1.1.1.1','208.67.222.222','2001:4860:4860::8888')
for ip in IPs:
    try:
        check = ipaddress.ip_address(ip)
        print(check)
        os.system(f"ping {ip}")
    except:
        print(invalidIP)