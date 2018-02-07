import socket, sys
from scapy.all import *

menu = r'''
-----------------------------------------

  #  Desenvolvido por Adriel Freud!
  #  Contato: businessc0ro2k17@gmail.com 
  #  FB: http://www.facebook.com/xrn401
  #   =>DebutySecTeamSecurity<=

-----------------------------------------

 $$$$$$\                                                             
$$  __$$\                                                            
$$ /  \__| $$$$$$$\ $$$$$$\  $$$$$$$\  $$$$$$$\   $$$$$$\   $$$$$$\  
\$$$$$$\  $$  _____|\____$$\ $$  __$$\ $$  __$$\ $$  __$$\ $$  __$$\ 
 \____$$\ $$ /      $$$$$$$ |$$ |  $$ |$$ |  $$ |$$$$$$$$ |$$ |  \__|
$$\   $$ |$$ |     $$  __$$ |$$ |  $$ |$$ |  $$ |$$   ____|$$ |      
\$$$$$$  |\$$$$$$$\\$$$$$$$ |$$ |  $$ |$$ |  $$ |\$$$$$$$\ $$ |      
 \______/  \_______|\_______|\__|  \__|\__|  \__| \_______|\__|  

-----------------------------------------
'''

def get_ttl(destino):
	try:
		ip = IP()
		ping = ICMP()
		ip.dst = destino
		send = sr1(ip/ping)
		if send.ttl == 64:
			print("""\n
			SISTEMA OPERACIONAL
				========= 
				= LINUX =
				=========
			\n\n""")
		elif send.ttl == 128:
			print("""\n
			SISTEMA OPERACIONAL
				===========
				= WINDOWS =
				===========
			\n\n""")
		elif send.ttl == 30:
			print("""\n
			SISTEMA OPERACIONAL
				===========
				= CYCLADES =
				===========
			\n\n""")
		elif send.ttl == 255:
			print("""\n
			SISTEMA OPERACIONAL
				===========
				= OPENBSD =
				===========
			\n\n""")
		else:
			print("[!] Impossivel Detectar Systema!\n\n")
	except:
		print("[!] Impossivel Detectar Systema!\n\n")

def scanner(ip, menu):
	print(menu+'\n')
	get_ttl(ip)
	portas_encontradas = []
	if 'http' or 'https' in ip:
		sobre_ip = ip.strip('https:/')
		ip = socket.gethostbyname(sobre_ip)

	for ports in range(0, 1180):
		client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		client.settimeout(0.03)
		code = client.connect_ex((ip, ports))

		if code == 0:
			portas_encontradas.append(ports)
			print("\n\n[STATUS] - Port %s OPEN!"%ports)
			try:
				print("[GRAB - SERVICE] - Service: %s\n"%socket.getservbyport(ports))
			except:
				print("[GRAB - SERVICE] - Service: NOT FOUND\n")
			client.close()

	print("[PORTAS ABERTAS] - %s"%portas_encontradas)
	print("\n[WARNING] Scan Terminado! - [Finish]\n")


if len(sys.argv) < 2:
	print(menu+'\n')
	print("\n[WARNING] - PARAMETROS INCORRETOS :) ")
	print("\nUse: root@localhost~# Scan.py 127.0.0.1\n")

else:	
	ip = sys.argv[1]
	scanner(ip, menu)
