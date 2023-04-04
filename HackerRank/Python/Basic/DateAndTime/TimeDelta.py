#!/bin/python3

import math
import os
import random
import re
import sys
from datetime import datetime, timedelta
# Complete the time_delta function below.
def time_delta(t1, t2):
        dtm1 = datetime.strptime(t1, '%a %d %b %Y %H:%M:%S %z')
        dtm2 = datetime.strptime(t2, '%a %d %b %Y %H:%M:%S %z')
        delta = (dtm1-dtm2).total_seconds()
        return str(int(abs(delta)))
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        t1 = input()

        t2 = input()

        delta = time_delta(t1, t2)

        fptr.write(delta + '\n')

    fptr.close()

