#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'birthday' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY s
#  2. INTEGER d
#  3. INTEGER m
#
def _subarray(s):
    result = []
    for i in range(len(s) + 1):
        for j in range(i):
            result.append(s[j: i])
    return result

def birthday(s, d, m):
    # Write your code here

    result = _subarray(s)
    new_lst = []
    for x in range(len(result)):
        if len(result[x]) == m:
            new_lst.append(result[x])
    sum1 = 0
    count = 0
    for y in range(len(new_lst)):
        sum1 = 0
        for z in range(len(new_lst[y])):
            
            sum1 += new_lst[y][z]
        
        if sum1 == d:
            count += 1
    return count
            
            

if __name__ == '__main__':
    

    n = int(input().strip())

    s = list(map(int, input().rstrip().split()))

    first_multiple_input = input().rstrip().split()

    d = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    result = birthday(s, d, m)


    print(result)

   
