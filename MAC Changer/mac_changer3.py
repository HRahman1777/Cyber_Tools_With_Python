#!/usr/bin/env python

import subprocess
import optparse

parser = optparse.OptionParser()

parser.add_option("-i", "--interface", dest="interface", help="Interface to change MAC address")
parser.add_option("-m", "--mac", dest="new_mac_add", help="New MAC address")

(options, arguments) = parser.parse_args()

interface = options.interface
new_mac_add = options.new_mac_add

print("[+] Changing MAC address for "+interface+" to "+new_mac_add)

subprocess.run(["ifconfig", interface, "down"])
subprocess.run(["ifconfig", interface, "hw", "ether", new_mac_add])
subprocess.run(["ifconfig", interface, "up"])


#OptionParser() is optparse module's class .. parser variable is now a object of a class
#parser's add_option method will handle the value / argument from user
#for an example #python3 mac_changer3.py --help .... will show the help
#parser's parse_args() will return the value what get from add_options agruments (line 11)
#like, value=interface, value=mac here options has interface and mac.. arguments has the value that user entered