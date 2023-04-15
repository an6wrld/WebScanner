import requests, builtwith
from colorama import Fore
import sys
def __start__():
    print(Fore.WHITE+" [!] Plase Enter Domain example.com")
    target = input(Fore.LIGHTRED_EX+" ┌─["+Fore.LIGHTRED_EX+" WebScanner"+Fore.LIGHTRED_EX+" ~ "+Fore.WHITE+"@HOME"+Fore.LIGHTRED_EX+"/"+Fore.WHITE+"IG"+Fore.LIGHTRED_EX+"/"+Fore.WHITE+"CMS-Detect "+Fore.LIGHTRED_EX+"""]
 └──╼ """+Fore.WHITE+"$ ")
    if not 'https://' in target or not 'http://' in target:
        target = 'http://'+target
    info = builtwith.parse(target)
    for name in info:
        value = ''
        for val in info[str(name)]:
            name = name.replace('-',' ')
            name = name.title()
            value += str(val) 
        print(Fore.WHITE+"\n"+name+': '+value)
    try:
        input(Fore.WHITE+" [-] Back To Menu (Press Enter...) ")
    except:
        print("")
        sys.exit()

