import socket, sys

menu = r'''
-----------------------------------------

  #  Desenvolvido por Adriel Freud!
  #  Contato: businessc0rp2k17@gmail.com 
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

def scanner(ip, menu):
	print(menu+'\n')
	portas_encontradas = []
	if 'http' or 'https' in ip:
		sobre_ip = ip.strip('https:/')
		ip = socket.gethostbyname(sobre_ip)

	for ports in range(0, 3306):
		client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		client.settimeout(0.03)
		code = client.connect_ex((ip, ports))

		if code == 0:
			portas_encontradas.append(ports)
			print("[STATUS] - Porta %s Aberta!\n"%ports)
			client.close()

	print("[PORTAS ABERTAS] - %s"%portas_encontradas)
	print("\n[WARNING] Scan Terminado! - [Finish]\n")


if len(sys.argv) < 2:
	print(menu+'\n')
	print("\n[WARNING] - PARAMETROS INCORRETOS :) ")
	print("Use: root@localhost~# Scan.py 127.0.0.1\n")

else:	
	print(sys.argv)
	ip = sys.argv[1]
	scanner(ip, menu)
