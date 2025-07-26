import ipaddress
import os

def GetByUser_string(value):
    value = input(f"Enter {value} ")
    return value

def GetByUser_int(value):
    value = int(input(f"Enter {value} "))
    return value

IPs = ()
while True:

    print("1: Add IP")
    print("2: ping all IPs")
    print("3: view all IPs")
    print("4: Exit")
    try:
        option = GetByUser_int("option")
        if option == 1:
            IP = GetByUser_string("IP address")
            try:
                check = ipaddress.ip_address(IP)
                print(f"the IP {check} has bees added")
                IPs = IPs + (IP,)
            except ValueError:
                print(f"invalid IP {IP}")
                continue
        if option == 2:
            print(f"Pinging all IPs {IPs}")
            if not IPs:
                print("There is no IP address added. First add an IP address.")
            else:
                for IP in IPs:
                    os.system(f"ping {IP}")
        if option == 3:
            print("All IPs are:")
            if not IPs:
                print("There is no IP address added. First add an IP address.")
            else:
                for IP in IPs:
                    print(IP)
        if option == 4:
            break
    except:
        print("Enter option 1-4 according to menu")
        continue