import requests
from bs4 import BeautifulSoup as bs

r=requests.get('https://stkapp.eu-gb.mybluemix.net/sample')
html=r.text
s=bs(html,'html.parser')
h=s.find_all(['h1','h2','h3','h4','h5','h6'])
spc="  "
for i in h:
    print(spc*(int(i.name[1])-1),end="")
    print(i.text.strip())

