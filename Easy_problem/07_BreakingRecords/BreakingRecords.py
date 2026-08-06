#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'breakingRecords' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.
#

def breakingRecords(scores):
    # Write your code here
    lowest = scores[0]
    highest = scores[0]
    lowest_break = 0
    higest_break = 0
    for i in range(len(scores)):
        if scores[i] < lowest:
            lowest_break += 1
            lowest = scores[i]
        elif scores[i] > highest:
            higest_break += 1
            highest = scores[i]
        
    return higest_break,lowest_break

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
