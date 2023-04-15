import os
import requests
import json
from colorama import Fore
import sys

def __start__():
        
        print (Fore.WHITE+"\n [!] Enter The Domain/ip\n")

        website = input(Fore.LIGHTRED_EX+" ┌─["+Fore.LIGHTRED_EX+" WebScanner"+Fore.LIGHTRED_EX+" ~ "+Fore.WHITE+"@HOME"+Fore.LIGHTRED_EX+"/"+Fore.WHITE+"IG"+Fore.LIGHTRED_EX+"/"+Fore.WHITE+"Reverse_IP "+Fore.LIGHTRED_EX+"""]
 └──╼ """+Fore.WHITE+"$ ")

        mysite = {"remoteAddress":website}

        link = requests.post("https://domains.yougetsignal.com/domains.php" , mysite)

        source = json.loads(link.content)

        print(source)


        for data in source["domainArray"]:
                print(" "+data[0]+"\n")

        try:

                input(Fore.WHITE+" [-] "+Fore.WHITE+"Back To Menu (Press Enter...) ")
        except:
                print("")
                sys.exit()
