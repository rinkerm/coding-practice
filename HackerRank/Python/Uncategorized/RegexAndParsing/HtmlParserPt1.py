from html.parser import HTMLParser
class HackerHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Start :",tag)
        for a in attrs:
            print("->",a[0],'>',a[1])
    def handle_endtag(self, tag):
        print("End   :",tag)
    def handle_startendtag(self, tag,attrs):
        print ("Empty :",tag)
        for a in attrs:
            print("->",a[0],'>',a[1])
    def handle_comment(self, data):
        return
parser = HackerHTMLParser()
n = int(input())
for i in range(0,n):
    parser.feed(input())
