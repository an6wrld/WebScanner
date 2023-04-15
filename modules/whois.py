import sys
import requests
from colorama import Fore


def __start__():
        try:
                print(Fore.WHITE+"\n [!] Plase Enter IP/Domain example.com\n")
                inp = input(Fore.LIGHTRED_EX+" ┌─["+Fore.LIGHTRED_EX+" WebScanner"+Fore.LIGHTRED_EX+" ~ "+Fore.WHITE+"@HOME"+Fore.LIGHTRED_EX+"/"+Fore.WHITE+"IG"+Fore.WHITE+"/"+Fore.WHITE+"Whois "+Fore.LIGHTRED_EX+"""]
 └──╼ """+Fore.WHITE+"$ ")
                result = requests.get('http://api.hackertarget.com/whois/?q=' + inp).text
                
                print(Fore.LIGHTGREEN_EZ+result)
                try:
                        input(Fore.WHITE+" [-] "+Fore.WHITE+"Back To Menu (Press Enter...) ")
                except:
                        print("")
                        sys.exit()  
        except:
                print("\nExit :)")