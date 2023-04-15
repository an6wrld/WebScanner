import sys
import requests
from colorama import Fore

def __start__():

        try:
                print(Fore.WHITE+"\n [!] Plase Enter IP/Domain\n")
                inp = input(Fore.LIGHTRED_EX+" ┌─["+Fore.LIGHTGREEN_EX+" WebScanner"+Fore.LIGHTRED_EX+" ~ "+Fore.WHITE+"@HOME"+Fore.LIGHTRED_EX+"/"+Fore.WHITE+"IG"+Fore.LIGHTRED_EX+"/"+Fore.WHITE+"Find-DNS "+Fore.LIGHTRED_EX+"""]
 └──╼ """+Fore.WHITE+"$ ")
                result = requests.get('https://api.hackertarget.com/findshareddns/?q=' + inp).text
                print(Fore.LIGHTGREEN_EX+result)
                try:
                        input(Fore.WHITE+" [-] "+Fore.WHITE+"Back To Menu (Press Enter...) ")
                except:
                        print("")
                        sys.exit()  
                
        except:
                print("\nExit :)")


