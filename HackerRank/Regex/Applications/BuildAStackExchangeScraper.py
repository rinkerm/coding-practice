import re
import sys

regex = '\/questions\/(\d+?)\/.*?>(.*?)<[\w\W]*?"relativetime">(.*?)<'

html = ''
for line in sys.stdin:
    html+=line

matches = re.findall(regex,html)

for match in matches:
    print('{};{};{}'.format(match[0],match[1],match[2]).strip())
