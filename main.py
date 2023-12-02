import os
hostname = "0.0.0.0" # Replace it by your IP / Domain
mac = "00:00:00:00:00:00" #Replace it by your MAC Address
response = os.system(f"ping -c 1 {hostname}")

if response != 0:
    print("Host Down")
    os.system(f"etherwake {mac}")
else:
    print("Host Up")
