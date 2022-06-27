import os

previousIp = '192.168.1.5'

externalIP  = os.popen('curl -s https://ifconfig.me').readline()

if externalIP != previousIp:
    print("You have a new external ip: ",externalIP)
else:
    print("Your external ip remains: ",externalIP)