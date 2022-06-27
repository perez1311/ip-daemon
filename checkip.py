import os


externalIP  = os.popen('curl -s https://ifconfig.me').readline()
print(externalIP)