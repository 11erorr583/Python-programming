# Create a script that reads logs from a text file and filters suspicious--mysqlserver
import re
suspicious_logs = []
with open("C:\\laragon\\bin\\apache\\httpd-2.4.62-240904-win64-VS17\\logs\\access.log",'r') as file:
    for line in file:
        if re.search(r"('|--|UNION|DROP|OR\s+1=1)",line):
            suspicious_logs.append(line)
            print("sqli recognized")
        if re.search(r"<script>",line):
            suspicious_logs.append(line)
            print("XSS detected")
        if re.search(r"javascript:",line):
            suspicious_logs.append(line)
            print("XSS detected")
        if re.search(r"on\w+\s*=",line):
            suspicious_logs.append(line)
            print("XSS detected")
        if re.search(r"%3Cscript%3E",line):
            suspicious_logs.append(line)
            print("XSS detected")
        if re.search(r"<.*?on\w+=.*?>",line):
            suspicious_logs.append(line)
            print("XSS detected")
        if re.search(r"/admin",line):
            suspicious_logs.append(line)
            print("unauthorized_access detected")
for row in suspicious_logs:
    print(row)