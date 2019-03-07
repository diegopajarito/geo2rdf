#from qgis.core import *
import os
import subprocess

print('lets try, yes its me')
os.system("ls -l")

test = subprocess.Popen(["ping","-W","2","-c", "1", "192.168.1.70"], stdout=subprocess.PIPE)
output = test.communicate()[0]


#https://stackoverflow.com/questions/3730964/python-script-execute-commands-in-terminal/3731000

# And now with geotriples
# Variables
geotriples = "geotriples-cmd"
action = "generate_mapping"
b_command = "-b"
base_uri = "'http://diana.test.co/repo/'"
o_command = "-o"
path_rml_file = "'/home/diego/Documents/Maps/geotriples/test_rml_py.rml'"
path_shp_file = "'/home/diego/Documents/Maps/geotriples/testgeotriples.shp'"

# geotriples-cmd generate_mapping -b http://test.caro.fi/repo/ -o '/home/diego/Documents/Maps/geotriples/test_rml.rml'  '/home/diego/Documents/Maps/geotriples/testgeotriples.shp'


test = subprocess.Popen([geotriples, action, b_command, base_uri, o_command, path_rml_file, path_shp_file], stdout=subprocess.PIPE)
output = test.communicate()[0]

print(output)

sentence = [geotriples, action, b_command, base_uri, o_command, path_rml_file, path_shp_file]
joined = ' '.join(sentence)
print(joined)

os.system(joined)