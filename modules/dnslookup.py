import sys
import requests
from colorama import Fore
import os
def __start__():

        try:
                print(Fore.WHITE+" [!] Enter The Domain example.com\n")
                inp = input(Fore.LIGHTRED_EX+" ┌─["+Fore.LIGHTGREEN_EX+" WebScanner"+Fore.LIGHTRED_EX+" ~ "+Fore.WHITE+"@HOME"+Fore.LIGHTRED_EX+"/"+Fore.WHITE+"IG"+Fore.LIGHTRED_EX+"/"+Fore.WHITE+"DNS-Lookup "+Fore.LIGHTRED_EX+"""]
 └──╼ """+Fore.WHITE+"$ ")
                result = requests.get('http://api.hackertarget.com/dnslookup/?q=' + inp).text
                print(Fore.LIGHTGREEN_EX+result)
                try:
                        input(Fore.WHITE+" [-] Back To Menu (Press Enter...) ")
                except:
                        print("")
                        sys.exit()
        except:
                print("\n Exit :)")
                sys.exit()

