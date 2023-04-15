import requests
import sys
import time
from colorama import Fore
search = ['robots.txt',
'search/',
'admin/',
'login/',
'sitemap.xml',
'sitemap2.xml',
'config.php',
'wp-login.php',
'log.txt',
'update.php',
'INSTALL.pgsql.txt',
'user/login/',
'INSTALL.txt',
'profiles/',
'scripts/',
'LICENSE.txt',
'CHANGELOG.txt',
'themes/',
'inculdes/',
'misc/',
'user/logout/',
'user/register/',
'cron.php',
'filter/tips/',
'comment/reply/',
'xmlrpc.php',
'modules/',
'install.php',
'MAINTAINERS.txt',
'user/password/',
'node/add/',
'INSTALL.sqlite.txt',
'UPGRADE.txt',
'INSTALL.mysql.txt']

def __start__():
    try:
        print(Fore.WHITE+" [!] Plase Enter WebSite Address \n")
        url = input(Fore.LIGHTRED_EX+" ┌─["+Fore.LIGHTRED_EX+" WebScanner"+Fore.LIGHTRED_EX+" ~ "+Fore.WHITE+"@HOME"+Fore.LIGHTRED_EX+"/"+Fore.WHITE+"IG"+Fore.LIGHTRED_EX+"/"+Fore.WHITE+"Robots_Scanner "+Fore.LIGHTRED_EX+"""]
 └──╼ """+Fore.WHITE+"$ ")
        if 'http' in url:
            pass
        elif 'http' != url:
            url = ('http://'+url)
            
        for i in search:
            time.sleep(0.1)

            ur = (url+"/"+i)
            "http://pythons.ir/robots.txt"
            reqs = requests.get(ur)
            if reqs.status_code == 200 or reqs.status_code == 405:
                print(Fore.LIGHTGREEN_EX+" [+] "+ ur)
            else:
                print(Fore.LIGHTRED_EX+" [-] "+ur)
        try:
            input(Fore.WHITE+" [-] "+Fore.WHITE+"Back To Menu (Press Enter...) ")
        except:
            print("")
            sys.exit()  
    except:
        print("")