#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#
grades=[]
length=int(input())
for _ in range(length):
    grades.append(int(input()))
final_result=[]
for i in grades:
    x=i
    if i % 5!=0 and i >35:
        while (x%5!=0):
            x=x+1
        if x%5==0 and x-i <3:
            final_result.append(x)
        else:
            final_result.append(i)
    else:
        final_result.append(x)
for a in final_result:
    print(a)
