import nmap
#First, you need a Postscanner object that will be used to do the scan
nm = nmap.PortScanner()
#You can then do a scan of all the IPV4 addresses provided by the network you are connected to
nm.scan(hosts = '192.168.2.1/24', arguments = '-sn')
for host in nm.all_hosts():
	#If the status of an IP address is not down, print it
	if nm[host]['status']['state'] != "down":
		print ("IPV4:", nm[host]['addresses']['ipv4'])
		#Print the MAC address
		try:
			print ("MAC ADDRESS:", nm[host]['addresses']['mac'])
		except:
			mac = 'unknown'
			print ("MAC ADDRESS:", mac)