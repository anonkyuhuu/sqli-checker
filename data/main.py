import requests as r
import os,sys,time

G = '\x1b[0;32m'
GL = '\x1b[32;1m'
B = '\x1b[0;36m'
P = '\x1b[35;1m'
BL = '\x1b[36;1m'
BD = '\x1b[34;1m'
R = '\x1b[31;1m'
W = '\x1b[37;1m'
H = '\x1b[30;1m'
Y = '\x1b[33;1m'
YL = '\x1b[1;33m'

logo=('''
\x1b[37;1m     (()__(()	      PLEASE NOT RECODE!
\x1b[37;1m     /       \  \x1b[36;1m     __  ____   ________  
\x1b[37;1m    ( /    \  \ \x1b[36;1m    /  |/  / | / /_  __/
\x1b[37;1m     \ \x1b[31;1mo o  \x1b[37;1m  / \x1b[36;1m   / /|_/ /| |/ / / / 
\x1b[37;1m     (_()_)__/ \ \x1b[36;1m /_/  /_/ |___/ /_/            
\x1b[37;1m    / _,==.____ \   
\x1b[37;1m   (   |--|\x1b[37;1m      ) \x1b[32;1m   Author\x1b[37;1m : sCuby07
\x1b[37;1m   /\_.|__|\x1b[37;1m'-.__/\_\x1b[32;1m   Team  \x1b[37;1m : Cyber Ghost ID
\x1b[37;1m  / (        /     \  \x1b[32;1mVerion \x1b[37;1m: 0.1
\x1b[37;1m  \  \      (      /
\x1b[37;1m   )  '._____)    /   \x1b[32;1mFungsi \x1b[37;1m: Test Vulns Web
\x1b[37;1m(((____.--(((____/
''')




def single_test():
	os.system('clear')
	print(logo)
	web = input('\n{}Target Web {}: '.format(YL,W))
	print("=" * 35)
	time.sleep(7)
	b = r.get(web+"%27").text
	if "You have an error in your SQL syntax" not in b:
		print("{}Not Vuln {}> {}".format(R,BL,web))
	else:
		print("{}Vuln {}> {}".format(GL,BL,web))

def multi_test():
	os.system('clear')
	print(logo)
	web = input('\n{}File : {}'.format(YL,W));print('=' * 35)
	time.sleep(7)
	t = open(web, 'r').readlines()
	for test in t:
		b = r.get(test+"%27").text
		if 'You have an error in your SQL syntax' in b:
			sys.stdout.write("\r{}Vuln {}> {}{}".format(GL,BL,W,test))
			time.sleep(5)
		else:
			sys.stdout.write("\r{}Not Vuln {}> {}{}".format(R,BL,W,test))
			time.sleep(5)


os.system('clear')
print(logo+"\n\n{}1){}. Single Test\n{}2){}. Multi Test\n".format(BL,W,BL,W))
w = input('Choose > {}'.format(GL))
if w == "1":
        single_test()

elif w == "2":
        multi_test()

else:
	exit('Please Input')
