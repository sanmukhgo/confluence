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
spc="   "

print("TABLE OF CONTENTS\n")
print((content[0].text.strip())[4:])
for i in range(1,len(content)):
    print(spc*(int(content[i].name[1])-1),end='')#puts indentation
    print(content[i].text.strip())#prints content
    if((i<len(content)-1) and (content[i].name[1]>content[i+1].name[1])):#puts newlines
        print()
