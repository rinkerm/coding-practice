import re
import sys

java_regex = r'java'
c_regex = r'#include'

s = ''
for line in sys.stdin:
    s+=line
    
if len(re.findall(java_regex,s))>0:
    print('Java')
elif len(re.findall(c_regex,s))>0:
    print('C')
else:
    print('Python')

