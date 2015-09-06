#!/usr/bin/env python3
import lookup

""" Reverse-DNS lookup tool for all North Korean IP addresses.
North Korean IP ranges are 175.25.176.0 - 175.45.179.255 and 
210.52.109.0 - 210.52.109.255 """

print("North Korean DNS Lookup Tool\nType 'help' for commands")
commandInput = input()
if commandInput == "help":
	pass

elif commandInput == "urllookup":
	url = input("Enter URL:")
	if lookup.lookup(url):
		print(url + " is hosted in North Korea.")
	elif lookup.lookup(url) is None:
		pass
	else:
		print("\033[1;42m" + url + " is not hosted in North Korea.\033[1;m")
	
