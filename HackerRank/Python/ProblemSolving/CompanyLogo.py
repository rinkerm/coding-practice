#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter


if __name__ == '__main__':
    s = input()
    c = Counter([char for char in s])
    l = sorted(list(c.items()),key = lambda x: (1/x[1],x[0]))
    print(l[0][0],l[0][1])
    print(l[1][0],l[1][1])
    print(l[2][0],l[2][1])
    
