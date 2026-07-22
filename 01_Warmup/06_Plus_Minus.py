#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    positave = 0
    negative = 0
    zero = 0
    
    total = len(arr)
    
    for i in range(len(arr)):
        if arr[i] < 0:
            negative += 1
        elif arr[i] > 0:
            positave += 1
            
        else:
            zero += 1
    positave_ratio = positave/total
    negative_ratio = negative/total
    zero_ratio = zero/total
    
    print(positave_ratio)
    print(negative_ratio)
    print(zero_ratio)
    
        

        
             
    # Write your code here

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
