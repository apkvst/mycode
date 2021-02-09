#!/usr/bin/env python3

from ipaddress import ip_address, IPv4Address, IPv6Address

ipchk = input('Apply an IP address: ') # this line now prompts the user for input

try:

   if ipchk == '192.168.70.1': # if a match on '192.168.70.1'
       # indented under if
       print('Looks like the IP address of the Gateway was set: ' + ipchk + ' This is not recommended.')
   elif type(ip_address(ipchk)) == IPv4Address: # if any data is provided, this will test true
       print("This is an IPv4 Address")
       print('Looks like the IP address was set: ' + ipchk) # indented under if
 
   elif type(ip_address(ipchk)) == IPv6Address:
        print(ipchk + " is an IPv6 Address. IPv4 address only")
   else: # if data is NOT provided
       print('You did not provide input.') # indented under else

except:
    print(ipchk + " is not an IP address.")
