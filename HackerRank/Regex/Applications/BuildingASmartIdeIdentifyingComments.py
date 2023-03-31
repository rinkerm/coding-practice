import re
import sys

regex = r'(?:(\/\/.*?)\n|(\/\*[\s\S]*?\*\/))'

code = ''
for line in sys.stdin:
    code += line.lstrip()

matches = re.findall(regex,code)
for match in matches:
    construct = (match[0]+match[1]).strip()
    print(construct)
