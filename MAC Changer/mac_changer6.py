#!/usr/bin/env python

import subprocess
import optparse
import re

def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Interface to change MAC address")
    parser.add_option("-m", "--mac", dest="new_mac_add", help="New MAC address")
    (options, arguments) = parser.parse_args()
    if not options.interface:
        parser.error("[-] Please specify an interface or use --help for more info.")
    elif not options.new_mac_add:
        parser.error("[-] Please specify a new mac address or use --help for more info.")
    return options


def change_mac(interface, new_mac_add):
    print("[+] Changing MAC address for " + interface + " to " + new_mac_add)
    subprocess.run(["ifconfig", interface, "down"])
    subprocess.run(["ifconfig", interface, "hw", "ether", new_mac_add])
    subprocess.run(["ifconfig", interface, "up"])

def get_current_mac(interface):
    ifconfig_res = subprocess.check_output(["ifconfig", interface])
    mac_add_finder = re.search(r"([0-9a-fA-F]{2}:){5}[0-9a-fA-F]{2}", str(ifconfig_res))
    if mac_add_finder:
        return mac_add_finder.group(0)
    else:
        print("[-] Could not read MAC address.")


option = get_arguments()
current_mac = get_current_mac(option.interface)
print("Current MAC address = "+ str(current_mac))
change_mac(option.interface, option.new_mac_add)
current_mac = get_current_mac(option.interface)
if current_mac == option.new_mac_add:
    print("[+] MAC address successfully changed to "+ current_mac)
else:
    print("[-] MAC address did not get changed.")
