
import socket
import termcolor

def scan(target, ports):
	print("Starting Scan for " + str(target))
	for port in range (1,ports+1):
		scan_port(target,port)

def scan_port(ipaddress,port):
	try:
		sock = socket.socket()
		sock.connect((ipaddress, port))
		print(" [+] Port Opened" + str(port))
		socket.close()
	except:
		pass

targets = input("[*] Enter Targets to Scan (split them by ,): ")
ports = int(input("[*] Enter How Many Ports You Want To Scan: "))
if ',' in targets:
	print("[*] Scanning Multiple Targets")
	for ip_addr in targets.split(','):
		scan(ip_addr.strip(" "), ports)
else: 
	scan(targets, ports)
