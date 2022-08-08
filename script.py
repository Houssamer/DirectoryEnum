import requests
import sys

with open('/home/rhuser/tryhackme/scripting/wordlist2.txt') as wordlist:
    dir_list  = wordlist.read().splitlines()
    
    for dir in dir_list:
        dir_url = f"http://{sys.argv[1]}/{dir}.html"
        r = requests.get(dir_url)
        if r.status_code == 404:
            pass
        else:
            print("Valid directory: ", dir_url)
