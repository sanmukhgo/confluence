""" Parses the Inventory Features page as "soup". """

from bs4 import BeautifulSoup as bs
import lxml
import html5lib


def _parse(location: str, parser: str):
    """
    Returns parsed page at "location as a BeautifulSoup object, 
    using the given parsers:

        lxml
        html5lib
        html.parser
    """
    try:
        f = open(location, "r")
        return bs(f.read(), parser)
    finally:
        f.close()


_html = "page/inventory.html"
_parser = "html5lib"

soup = _parse(_html, _parser)

"""Prints the page, if invoked directly."""
if __name__ == "__main__":
    print(soup.prettify)
