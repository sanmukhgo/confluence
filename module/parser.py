import requests
from bs4 import BeautifulSoup as bs
import lxml
import html5lib

""" Parses the Inventory Features page into soup."""


def parse(url, parser='html.parser', payload={}):
    """
    Parses the webpage using the given parser.
    Parsers:
        lxml
        html5lib
        html.parser
    """

    req = requests.post(url, data=payload)
    html = req.text
    return bs(html, parser)


_payload = {'os_username': 'sanmukh.s',
            'os_password': 'Grey@1234'}
_url = 'https://work.greyorange.com/confluence/display/BS/40.+Inventory+Features'

soup = parse(_url, 'html5lib', _payload)
