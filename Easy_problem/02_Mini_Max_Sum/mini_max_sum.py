#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    # Write your code here
    
    temp = 0
    
    
    
    for i in range(len(arr)):
        temp = temp + arr[i]
    
    min_sum = temp - arr[0]
    max_sum = temp - arr[0]
        
   
    for i in range(len(arr)):
        curr = temp - arr[i]
        if curr < min_sum:
            min_sum = curr
            
        elif curr > max_sum:
            max_sum =curr
    print(min_sum,max_sum)
        
        
           
        
        

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
