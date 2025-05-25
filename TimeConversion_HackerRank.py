#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here
    if s[len(s) - 2] == 'A':
        if s[0] + s[1] == '12':
            return '00' + s[2:len(s)-2]
        return s[:len(s)-2]
    else:
        if s[0] + s[1] == '12':
            return s[:len(s)-2]
        else:
            pm = s[0] + s[1]
            num = int(pm)
            num += 12
            return str(num) + s[2:len(s)-2]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()