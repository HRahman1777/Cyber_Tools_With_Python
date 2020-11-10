#!/usr/bin/env python

import subprocess

interface = input("interface > ")
new_mac_add = input("new MAC > ")

print("[+] Changing MAC address for "+interface+" to "+new_mac_add)

subprocess.run(["ifconfig", interface, "down"])
subprocess.run(["ifconfig", interface, "hw", "ether", new_mac_add])
subprocess.run(["ifconfig", interface, "up"])
