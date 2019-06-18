import requests
from bs4 import BeautifulSoup as bs
import lxml
import html5lib
import pytest 

url = 'https://work.greyorange.com/confluence/display/BS/40.+Inventory+Features'
payload = {'os_username': 'sanmukh.s',
           'os_password': 'Grey@1234'}
req = requests.post(url, data=payload)

def test_request():
    code = req.status_code
    assert code == 200

def test_login():
    assert req.cookies
