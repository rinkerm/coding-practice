import sys
import math

line = sys.stdin.readline().strip().split(" ")
articles = int(line[0])
factor = int(line[1])-0.99
bribes = math.ceil(articles*factor)
print(bribes)
