import requests
import os
import bcolors
import sys,argparse


def banner():
    print("""

                           
                ██╗░░██╗██╗██████╗░██████╗░███████╗███╗░░██╗░░░░░░████████╗██████╗░███████╗░█████╗░░██████╗██╗░░░██╗██████╗░███████╗
                ██║░░██║██║██╔══██╗██╔══██╗██╔════╝████╗░██║░░░░░░╚══██╔══╝██╔══██╗██╔════╝██╔══██╗██╔════╝██║░░░██║██╔══██╗██╔════╝
                ███████║██║██║░░██║██║░░██║█████╗░░██╔██╗██║█████╗░░░██║░░░██████╔╝█████╗░░███████║╚█████╗░██║░░░██║██████╔╝█████╗░░
                ██╔══██║██║██║░░██║██║░░██║██╔══╝░░██║╚████║╚════╝░░░██║░░░██╔══██╗██╔══╝░░██╔══██║░╚═══██╗██║░░░██║██╔══██╗██╔══╝░░
                ██║░░██║██║██████╔╝██████╔╝███████╗██║░╚███║░░░░░░░░░██║░░░██║░░██║███████╗██║░░██║██████╔╝╚██████╔╝██║░░██║███████╗
                ╚═╝░░╚═╝╚═╝╚═════╝░╚═════╝░╚══════╝╚═╝░░╚══╝░░░░░░░░░╚═╝░░░╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝╚═════╝░░╚═════╝░╚═╝░░╚═╝╚══════╝
                                                                                                              Code by NG          
          """)

if len(sys.argv) > 1:
    banner()
    if ((sys.argv[1] == '-u') | (sys.argv[1] == '-o')):
            try:
                input_url = sys.argv[2]
                input_location = sys.argv[4]

                https_url = "https://"+input_url

                parser = argparse.ArgumentParser()
                parser.add_argument("-u", required=True)
                parser.add_argument("-o", required=True)
                args = parser.parse_args()

                if(os.path.exists(input_location)==True):
                    status_url = requests.get(https_url).status_code

                file = open(input_location, "r")
                for x in file:
                    url_dir= https_url+"/"+x
                    if(requests.get(url_dir).status_code == 200):
                        print(bcolors.OKMSG)
                        print(requests.get(https_url).status_code,url_dir)
            except:
                print(bcolors.ERR + "Please enter valid url with valid word list location")
                print(bcolors.ERR + "Enter the URL without https:// or http://")

    elif ((sys.argv[1] == '-h') | (sys.argv[1] == '--help')):
            print(bcolors.BOLD + 'usage: hidden-treasure.py [-h] -d DOMAIN' '\n' 'OPTIONS:' '\n' '-h,--help    '
                                 'show this help message and exit' '\n''-u URL,   --url URL' '\n' '-o wordlist    :Location of Wordlist')

    elif (((sys.argv[1] != '-u') | (sys.argv[1] != '-o'))):
        print('Please enter -u <valid url without http:// or https://> -o <location of WordList>')
else:
    banner()
    print(bcolors.ERR + 'Please select at-least 1 option from (-u,-o) or -h, with a valid URL')
