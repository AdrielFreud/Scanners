/*
# Desenvolvido por Adriel Freud!
# Contato: usuariocargo2016@gmail.com 
# FB: http://www.facebook.com/xrn401
#   =>DebutySecTeamSecurity<=
*/

#include <stdio.h>
#include <stdlib.h>
#include <netdb.h>
#include <time.h>
#define inithread() time_t rawtime; struct tm * timeinfo;time(&rawtime);timeinfo=localtime(&rawtime); printf("\t%s\n", asctime(timeinfo));
void fatal(char *mnsg){fprintf(stderr, "[WARNING] - %s", mnsg);exit(EXIT_FAILURE);}

int main(int argc, char *argv[]){

	int meusocket;
	int conecta;
	int port;
	int inicio = 0;
	int final = 1024;
	char *destino = argv[1];
	struct sockaddr_in alvo;

	if (argc < 2){
		fatal("\n\t=> AdrielFreud <=\n\nUSAGE: root@localhost~# ./scan IP // 192.168.0.100\n");
	}else{
		fatal("Init THREADING on:");
		inithread();
	    for(port=inicio; port < final; port++){
	     	meusocket = socket(AF_INET, SOCK_STREAM, 0); 
	        alvo.sin_family = AF_INET;
	        alvo.sin_port = htons(port);
	        alvo.sin_addr.s_addr = inet_addr(destino);
		    conecta = connect(meusocket, (struct sockaddr *)&alvo, sizeof alvo);

		    if(conecta == 0){
	            printf("[!] Porta %d - Status [ABERTA]\n",port);
	        	close(meusocket);
	            close(conecta);
	        }else{
	            close(meusocket);
	            close(conecta);
		    }
		}
	}
	return EXIT_SUCCESS;
}