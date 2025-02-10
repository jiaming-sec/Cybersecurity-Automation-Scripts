import re

def extract_ips(log_file):
    with open(log_file, 'r') as file:
        logs = file.read()
    return re.findall(r'\b(?:\d{1,3}\.){3}\d{1,3}\b', logs)

log_file = "server.log"
ip_addresses = extract_ips(log_file)
print("Extracted IPs:", ip_addresses)

