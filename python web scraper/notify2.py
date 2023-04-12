import requests
from bs4 import BeautifulSoup
import difflib
import time
from datetime import datetime

# target url 
url="https://excelfiles.space/en/python-en/python-script-to-monior-changes-on-a-webpage"
# act like a browser 
headers={'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

prevVersion=""
FirstRun=True
while True:
    # download the page 
    response=requests.get(url,headers=headers)
    # parse the downloaded homepage
    soup=BeautifulSoup(response.text,'lxml')

    # remove all scripts and styles 
    for script in soup(['script','style']):
        script.extract()
    soup=soup.get_text()
    # compare the page text to previous version 
    if prevVersion!=soup:
        # on the first run-just memorize the page 
        if FirstRun==True:
            prevVersion=soup
            FirstRun=False
            print("start monitoring "+url+ ""+str(datetime.now()))
        else:
            print("changes detected at: "+str(datetime.now()))    
            OldPage=prevVersion.splitlines()
            NewPage=soup.splitlines()
            # compare versions and highlight changes using difflib 
            d=difflib.differ()
            diff=d.compare(OldPage,NewPage)
            out_text="\n".join([ll.rstrip() for ll in '\n'.join(diff).splitlines() if ll.strip() ])
            print(out_text)
            OldPage=NewPage
            prevVersion=soup
    else:
        print("no changes "+str(datetime.now()))
    time.sleep(300)
    continue