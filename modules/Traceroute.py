import sys
import requests
from colorama import Fore

def __start__():
        try:
                
                print(Fore.while+" [!] Plase Enter Domain example.com")
                inp = input(Fore.LIGHTRED_EX+" ┌─["+Fore.LIGHTRED_EX+" WebScanner"+Fore.LIGHTRED_EX+" ~ "+Fore.WHITE+"@HOME"+Fore.LIGHTRED_EX+"/"+Fore.WHITE+"IG"+Fore.LIGHTRED_EX+"/"+Fore.WHITE+"TraceRoute "+Fore.LIGHTRED_EX+"""]
 └──╼ """+Fore.WHITE+"$ ")
                result = requests.get('https://api.hackertarget.com/mtr/?q=' + inp).text
                print(result)
                try:
                        input(Fore.WHITE+" [-] "+Fore.WHITE+"Back To Menu (Press Enter...) ")
                except:
                        print("")
                        sys.exit()  
        except:
                print("\nExit :)")
                
        
