#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countApplesAndOranges' function below.
#
# The function accepts following parameters:
#  1. INTEGER s
#  2. INTEGER t
#  3. INTEGER a
#  4. INTEGER b
#  5. INTEGER_ARRAY apples
#  6. INTEGER_ARRAY oranges
s,t=map(int,input().split())
a,b=map(int,input().split())
m,n=map(int,input().split())
apples = list(map(int, input().rstrip().split()))
oranges = list(map(int, input().rstrip().split()))
finalapp=[]
finalora=[]
for each_apple in apples:
    tot=a+(each_apple)
    finalapp.append(tot)
for each_orange in oranges:
    tot=b+(each_orange)
    finalora.append(tot)
countapp=0
countora=0
for i in finalapp:
    if i >= s and i <=t:
        countapp=countapp+1
for i in finalora:
    if i >= s and i <=t:
        countora=countora+1
print(countapp)
print(countora)
