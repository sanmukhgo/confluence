from bs4 import BeautifulSoup as bs

s=bs(open("sample.html"),'html.parser')
h1=s.h1.text.strip()
h2=s.h1.text
print(h1)
print(h2)

