# Create a script that reads logs from a text file and filters suspicious--windows defender
import re
count = 0
with open("C:\\Windows\\System32\\LogFiles\\Firewall\\pfirewall.log",'r')as file:
    for line in file:
        if re.search("DROP",line):
            print("suspicious_activity found!!")
            print(line)
        if re.search("ICMP",line):
            count+=1
if count>100:
    print("ping flood found ICMP count is",count)