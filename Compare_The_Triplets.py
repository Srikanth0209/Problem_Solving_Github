#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the compareTriplets function below.
def compareTriplets(a, b):
    aliceArray=a
    bobArray=b
    points0falice=0
    points0fbob=0
    for i in range (len(aliceArray)):
        if aliceArray[i] > bobArray[i]:
            points0falice+=1
        elif bobArray[i] > aliceArray[i]:
            points0fbob+=1
        else:
            continue
    return [points0falice,points0fbob]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
