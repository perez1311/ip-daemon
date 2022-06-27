import os

previousIp

externalIP  = os.popen('curl -s https://ifconfig.me').readline()

if externalIP != previousIp:
    print("You have a new external ip: ",externalIP)
else:
    print("Your external ip remains: ",externalIP)