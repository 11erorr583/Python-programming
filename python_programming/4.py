#'Create a script that takes 5 IP addresses and stores them in a
# 'tuple'''
import ipaddress
IPs = ()
for a in range(5):
    a = input(" Enter IP address ")
    try:
        IP=ipaddress.ip_address(a)
        IPs = IPs + (a,)
        print(IPs)
    except ValueError:
        print("invalidIP")
print(IPs)