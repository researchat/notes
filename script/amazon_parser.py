from html.parser import HTMLParser
import re
import urllib.request
class MyHTMLParser(HTMLParser):

#    def __init__(self):
#        super().__init__()
#        self.found_tag = False
#        self.comic_info = []

    def handle_starttag(self, tag, attrs):
        print("Encountered a start tag:", tag)

        #if re.match('span', tag) and self.kansuu in d.get('id',''):
        #    print ('got it')
        #    self.found_tag = True

    def handle_endtag(self, tag):
        print("Encountered an end tag :", tag)

    def handle_data(self, data):
        pass
#        print("Encountered some data  :", data)
        #if self.found_tag:
        #    self.comic_info.append(data)
        #    self.found_tag = False

#    def feed(self, content, kansuu ='collection-size', kann = ''):
#        self.kansuu = kansuu
#        self.kann = kann
#        super().feed(content)

url = 'https://www.amazon.co.jp/gp/product/B07R8GQ8DZ'
request = urllib.request.Request(url)
with urllib.request.urlopen(request) as htmldata:
    parser = MyHTMLParser()
    parser.feed(htmldata.read().decode('utf-8'))
#    print (parser.comic_info)

