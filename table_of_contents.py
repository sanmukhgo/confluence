import requests
from bs4 import BeautifulSoup as bs
import lxml
import html5lib

payload = {'os_username': 'sanmukh.s', 'os_password': 'Grey@1234'}
url = 'https://work.greyorange.com/confluence/display/BS/40.+Inventory+Features'

r=requests.post(url, data=payload)
html=r.text
soup=bs(html,'html5lib')

m=soup.find('div',{'id':'main'})
content=m.find_all(['h1','h2','h3','h4','h5','h6'])
spc="   "   #tab space

print("TABLE OF CONTENTS:\n")
print((content[0].text.strip())[4:])
l=len(content)

for i in range(1,l):
    hn1=int(content[i].name[1])
    print(spc*(hn1-1),end='')       #puts indentation
    print(content[i].text.strip())  #prints content
    try:
        hn2=int(content[i+1].name[1])
    except:
        pass
    else:
        if (i<l-1) and (hn1>hn2):   #puts newlines
            print()


