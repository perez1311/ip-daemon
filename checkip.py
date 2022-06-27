import os
checkServer = https://ifconfig.me


externalIP  = os.popen('curl -s ',checkServer).readline()
print(externalIP)