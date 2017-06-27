from html.parser import HTMLParser
from urllib import Parser

class FindLinks(HTMLParser):

    def __init__(self):
        super().__init__()

    def error(self, message):
        pass
        
    def handle_starttag(self, tag, attrs):
        print(tag)
        
finder = FindLinks()
finder.feed("<HTML><HEAD><TITLE>Test</TITLE></HEAD></HTML>")
