from HTMLParser import HTMLParser
import os

# create a subclass and override the handler methods
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print "Encountered a start tag:", tag

    def handle_endtag(self, tag):
        print "Encountered an end tag :", tag

    def handle_data(self, data):
        print "Encountered some data  :", data

# instantiate the parser and fed it some HTML
dir = os.path.dirname(__file__)
parser = MyHTMLParser()

filename = os.path.join(dir, 'even_shorter.htm')

parser = MyHTMLParser()

with open(filename, 'r') as content_file:
    content = content_file.read()
    parser.feed(content)
