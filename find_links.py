from html.parser import HTMLParser
from urllib import Parser

class FindLinks(HTMLParser):

    def __init__(self,base_url):
        super().__init__()
        self.base_url

    def error(self, message):
        pass
        
    def handle_starttag(self, tag, attrs):
        links = set()
        if tag == 'a':
            for (name, value) in attrs:
                if name == 'href':
                    if value == '/%':
                        value = base_url + value
                    links.add(value)
        return links
        
testing = FindLinks()
testing.feed("<HTML><HEAD><TITLE>Test</TITLE></HEAD></HTML>")
