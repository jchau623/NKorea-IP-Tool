import socket
import traceback
import re

if __name__ == '__main__':
	print("Run nkdns.py instead.")

def lookup(url):
	"""Translate a URL to IP address. Tells you if
	host server is a North Korean server."""
	try:
		ip_addr = socket.gethostbyname(url)
		print(ip_addr)
		return NKIPChecker(ip_addr)
	except:
		traceback.print_exc()
		return None

def NKIPChecker(ip_addr):
	"""Checks if the IP address given is part
	of the North Korean IP space"""
	#As an exercise to myself, I won't use urllib
	NKIPRange = re.compile('(175\.([2-3][0-9]|4[0-5])\.17[6-9]\.(1?[0-9]{1,2}|2[0-5]{2}))|(210\.52\.109\.(1?[0-9]{1,2}|2[0-5]{2}))')
	return True if NKIPRange.match(ip_addr) is not None else False
	
