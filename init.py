#from qgis.core import *
import os
import subprocess

print('lets try, yes its me')
os.system("ls -l")
print('lets try, now the path')
os.system("pwd")

print('lets try, now as variable')
txt_out = os.system("pwd")

#print('The value of txt_out is: ' + txt_out)


test = subprocess.Popen(["ping","-W","2","-c", "1", "192.168.1.70"], stdout=subprocess.PIPE)
output = test.communicate()[0]

print(test)

#https://stackoverflow.com/questions/3730964/python-script-execute-commands-in-terminal/3731000