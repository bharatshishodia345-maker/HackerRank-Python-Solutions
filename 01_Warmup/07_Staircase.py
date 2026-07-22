#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'staircase' function below.
#
# The function accepts INTEGER n as parameter.
#

def staircase(n):
    t = n
    for i in range(0,t):
        for j in range(0,t):
            if j >= t - i - 1:
                print('#', end = '')
            else:
                print(' ', end='')  
        print()  
                
            
    # Write your code here

if __name__ == '__main__':
    n = int(input().strip())

    staircase(n)
