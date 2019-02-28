#!/usr/bin/env python
import subprocess
import optparse
import re

def get_arguments():
	parser = optparse.OptionParser()
	parser.add_option("-i", "--interface", dest="interface", help="interface selection")
	parser.add_option("-m", "--mac", dest="mac", help="New MAC selection")
	(options, arguments) = parser.parse_args()
	if  not options.interface:
		parser.error("[-] Please specify an interface, use --help for more info.")
	elif not optons.mac:
		parser.error("[-] Pleasespecify a new MAC address, use -- help for more info.")
	return options
def change_mac(interface, mac):
	print("[+] Change MAC address for " + interface + " to " + mac)
	subprocess.call(["ifconfig", interface, "down"])
	subprocess.call(["ifconfig", interface, "hw", "ether", mac])
	subprocess.call(["ifconfig", interface, "up"])

def get_current_mac(interface):
	ifconfig_result = subprocess.check_output(["ifconfig", interface])
	mac_address_search_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_result)
	if mac_address_search_result:
		return mac_address_search_result.group(0)
	else:
		print("[-] sorry could not get ac address")
options= get_arguments()
current_mac =get_current_mac(options.interface)
print("current MAC = " + str(current_mac))
change_mac(options>.interface, options.mac)