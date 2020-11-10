#!/usr/bin/env python

import subprocess

interface = input("interface > ")
new_mac_add = input("new MAC > ")

print("[+] Changing MAC address for "+interface+" to "+new_mac_add)

subprocess.run("ifconfig "+interface+" down", shell=True)
subprocess.call("ifconfig "+interface+" hw ether "+new_mac_add, shell=True)
subprocess.call("ifconfig "+interface+" up", shell=True)



#  note
#call modules function used for old version, run is more updated 