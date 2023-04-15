import requests
import os
import sys
import ipapi
from colorama import Fore

def __start__():
    print(Fore.WHITE+"\n [!] Enter IP Address")
    print(Fore.WHITE+"\n [/] Or Press The Enter Key :))) \n")
    
    site = input(Fore.LIGHTRED_EX+" ┌─["+Fore.LIGHTRED_EX+" WebScanner"+Fore.LIGHTRED_EX+" ~ "+Fore.WHITE+"@HOME"+Fore.LIGHTRED_EX+"/"+Fore.WHITE+"IG"+Fore.LIGHTRED_EX+"/"+Fore.WHITE+"IP-Location "+Fore.LIGHTRED_EX+"""]
 └──╼ """+Fore.WHITE+"$ ")
    source = ipapi.location(ip=site, key=None, field=None)
    try:
        print(Fore.WHITE+" [!]"+Fore.LIGHTGREEN_EX+" See your info")
        print (Fore.WHITE+" [!]"+Fore.LIGHTGREEN_EX+" ip = "+ source["ip"])
        print (Fore.WHITE+" [!]"+Fore.LIGHTGREEN_EX+" city = " + source["city"])
        print (Fore.WHITE+" [!]"+Fore.LIGHTGREEN_EX+" region = "+ source["region"])
        print (Fore.WHITE+" [!]"+Fore.LIGHTGREEN_EX+" id country = "+source["country"])
        print (Fore.WHITE+" [!]"+Fore.LIGHTGREEN_EX+" country = "+ source["country_name"])
        print (Fore.WHITE+" [!]"+Fore.LIGHTGREEN_EX+" Calling Code = "+source["country_calling_code"])
        print (Fore.WHITE+" [!]"+Fore.LIGHTGREEN_EX+" Languages = "+source["languages"])
        print (Fore.WHITE+" [!]"+Fore.LIGHTGREEN_EX+" org = "+ source["org"])
        try:
            input(Fore.WHITE+" [-] "+Fore.WHITE+"Back To Menu (Press Enter...) ")
        except:
            print("")
            sys.exit()  
    except:
        print(Fore.RED+"Sorry Please Enter IP Address")

