#!/bin/python3

import math
import os
import random
import re
import sys


regex = r'(?<=[A-Za-z\d])[^A-Za-z\d]+(?=[A-Za-z\d])'

first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

m = int(first_multiple_input[1])

matrix = []

for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)
s = ''
for i in range(0,m):
    for j in range(0,n):
        s= s+matrix[j][i:i+1]
s = re.sub(regex,' ',s)
print(s)
