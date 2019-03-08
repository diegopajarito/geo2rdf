# Licence: CC-BY
# Description: This script serves to test the execution of console-based 
# commands from QGIS. In particular the use of geotriples jar
# Tested only for Ubuntu and QGIS 3
#
# Comments: It requires geotriples jar to be installed. Geotriples instructions
# used are here: https://github.com/LinkedEOData/GeoTriples/wiki
# Authors: Carolina Figueroa - Diego Pajarito 

import subprocess
from qgis.core import *
import qgis.utils

# Setting up the input values
lyr_name = 'sint'

# To git test again

# Setting up the veariables needed by geotriples

geotriples = 'geotriples-cmd'
action = "generate_mapping"
b_command = "-b"
base_uri = "%r" % 'http://diana.test.co/repo/'
o_command = "-o"
path_rml_file = "%r" % '/home/diego/Documents/Maps/geotriples/test_rml_py.rml'


lyr = QgsProject.instance().mapLayersByName(lyr_name)
if lyr:
    lyr_path = lyr[0].dataProvider().dataSourceUri()
    path, sep, tail = lyr_path.partition('|')
    lyr_path = "%r" % path

    # Now call the command
    sentence = [geotriples, action, b_command, base_uri, o_command, path_rml_file, lyr_path]
    joined = ' '.join(sentence)
    print(joined)
    sbp = subprocess.Popen([geotriples, action, b_command, base_uri, o_command, path_rml_file, lyr_path], stdout=subprocess.PIPE)
    output = sbp.communicate()[0]
    print(output)
    
else:
    print('Error: No layer found')
    
