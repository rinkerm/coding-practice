import re
langstring = 'C:CPP:JAVA:PYTHON:PERL:PHP:RUBY:CSHARP:HASKELL:CLOJURE:BASH:SCALA:ERLANG:CLISP:LUA:BRAINFUCK:JAVASCRIPT:GO:D:OCAML:R:PASCAL:SBCL:DART:GROOVY:OBJECTIVEC'
langs = langstring.split(':')
regex = r'^[1-9]\d{4}\s(\w+)$'

n = int(input())

for i in range(0,n):
    s = input()
    match = re.findall(regex,s)
    if len(match) > 0 and match[0] in langs:
        print('VALID')
    else:
        print('INVALID')
        
