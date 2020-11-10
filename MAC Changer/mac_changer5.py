#!/usr/bin/env python

import subprocess
import optparse


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


option = get_arguments()
change_mac(option.interface, option.new_mac_add)
