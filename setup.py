#!/usr/bin/python3

from os import system,path
from termcolor import cprint,colored

system("clear"),print("""\033[90m
░█████╗░░░░░░███╗░░░█████╗░██████╗░░█████╗░███████╗░█████╗░
██╔══██╗░░░░████║░░██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔══██╗
██║░░██║░░░██╔██║░░███████║██████╔╝███████║█████╗░░███████║
██║░░██║░░░╚═╝██║░░██╔══██║██╔══██╗██╔══██║██╔══╝░░██╔══██║
╚█████╔╝██╗███████╗██║░░██║██║░░██║██║░░██║██║░░░░░██║░░██║
░╚════╝░╚═╝╚══════╝╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝
\033[00m\033[91m
░█████╗░██╗░░░░░██╗░░░░░  ██████╗░░█████╗░░██████╗
██╔══██╗██║░░░░░██║░░░░░  ██╔══██╗██╔══██╗██╔════╝
███████║██║░░░░░██║░░░░░  ██║░░██║██║░░██║╚█████╗░
██╔══██║██║░░░░░██║░░░░░  ██║░░██║██║░░██║░╚═══██╗
██║░░██║███████╗███████╗  ██████╔╝╚█████╔╝██████╔╝
╚═╝░░╚═╝╚══════╝╚══════╝  ╚═════╝░░╚════╝░╚═════╝░
\033[00m\033[90m
██╗███╗░░██╗░██████╗████████╗░█████╗░██╗░░░░░██╗░░░░░███████╗██████╗░
██║████╗░██║██╔════╝╚══██╔══╝██╔══██╗██║░░░░░██║░░░░░██╔════╝██╔══██╗
██║██╔██╗██║╚█████╗░░░░██║░░░███████║██║░░░░░██║░░░░░█████╗░░██████╔╝
██║██║╚████║░╚═══██╗░░░██║░░░██╔══██║██║░░░░░██║░░░░░██╔══╝░░██╔══██╗
██║██║░╚███║██████╔╝░░░██║░░░██║░░██║███████╗███████╗███████╗██║░░██║
╚═╝╚═╝░░╚══╝╚═════╝░░░░╚═╝░░░╚═╝░░╚═╝╚══════╝╚══════╝╚══════╝╚═╝░░╚═╝\033[00m\n""")
End="\n"+"\033[95m\033[01m#"*50+"\033[00m\n"

def pather(file,cloner):
	if path.exists(file): 
		cprint("[++] "+file+ " already installed","green",attrs=["bold"])
	else:
		system(f"sudo git clone {cloner}")
		cprint("[++] "+file+" installed successfully","green",attrs=["bold"],end=End)

cprint("[+] Installing 0.1ArafaDoS...","cyan",attrs=["bold"])
pather("0.1ArafaDoS","https://github.com/0Arafa/0.1ArafaDoS.git")
cprint("[+] Installing slowloris...","cyan",attrs=["bold"])
system("sudo pip3 install slowloris")
cprint("[++] slowloris installed successfully","green",attrs=["bold"],end=End)
cprint("[+] Installing goldeneye...","cyan",attrs=["bold"])
system("sudo apt install goldeneye")
cprint("[++] goldeneye installed successfully","green",attrs=["bold"],end=End)
cprint("[+] Installing torshammer...","cyan",attrs=["bold"])
pather("torshammer","https://github.com/dotfighter/torshammer.git")
cprint("[+] Installing XERXES...","cyan",attrs=["bold"])
pather("XERXES","https://github.com/XCHADXFAQ77X/XERXES.git")
system("cd XERXES&&gcc -o xerxes xerxes.c&&cd ..")
rudy_issue="\033[96m[!] If rudy isn't installed, use a VPN like openvpn or nipe and run this command ' sudo npm install -g rudyjs '\033[00m"
cprint("[+] Installing rudy...","cyan",attrs=["bold"])
system("sudo npm install -g rudyjs")
cprint("[++] rudy installed successfully\n","green",attrs=["bold"],end=rudy_issue+End)
cprint("\n"+" "*5+"#"*5+" "*3,"white",attrs=["bold"],end="")
cprint("This tool is designed for ethical purpose, I'm not responsible for any unethical activity","blue",attrs=["bold","blink"],end="")
cprint(" "*3+"#"*5+"\n","white",attrs=["bold"])

#By: Abd Almoen Arafa (0.1Arafa)
#Age: 15
