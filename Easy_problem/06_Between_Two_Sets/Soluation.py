#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getTotalX' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def getTotalX(a, b):
    start = max(a)
    end = min(b)

    count = 0

    for num in range(start, end + 1):

        valid = True

        # Check if every element of a is a factor of num
        for i in a:
            if num % i != 0:
                valid = False
                break

        # If first condition failed, check next number
        if not valid:
            continue

        # Check if num is a factor of every element of b
        for j in b:
            if j % num != 0:
                valid = False
                break

        # If both conditions are true
        if valid:
            count += 1

    return count
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    fptr.write(str(total) + '\n')

    fptr.close()
