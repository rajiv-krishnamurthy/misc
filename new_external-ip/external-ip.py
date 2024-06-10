import requests
from datetime import datetime

#check if a file called ./cfg.cfg exists, if not exit the program. If the file exists, read the first line and if that directory does not exists then exit the program
try:    
    with open('cfg.cfg', 'r') as cfg_file:
        file_path = cfg_file.read().strip()
        try:
            with open(file_path, 'w') as file:
                pass
        except FileNotFoundError:
            print(f"File path {file_path} does not exist.")
            exit(1) 
except FileNotFoundError:
    print(f"This script expects a file cfg.cfg in the same directory, it does not exist.")
    exit(1)    

# Make a request to an API that returns the external IP
response = requests.get('https://api.ipify.org?format=json')

# Get the IP address from the response
ip_address = response.json()['ip']

# Write the date and time now and the IP address to a file
current_datetime = datetime.now()
formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
#file_path = "/Users/rjk/Library/Mobile Documents/com~apple~CloudDocs/external-ip.txt"

# Read the file path from cfg.cfg
with open('cfg.cfg', 'r') as cfg_file:
    file_path = cfg_file.read().strip()

with open(file_path, 'w') as file:
    file.write(f"{formatted_datetime} : {ip_address}")

# Print the external IP address
print(f"External IP address: {ip_address}")
