#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the decentNumber function below.
def decentNumber(n):
    three = n//3
    
    while (n - 3*three)%5 != 0:
        three -= 1
        
    if three > 0:
        res = [5] * 3 * three
        res += [3] * (n - 3*three)
    elif three == 0 and n%5 == 0:
        res = [3] * n
    else:
        res = [-1]
        
    return res
        

if __name__ == '__main__':
    t = int(input().strip())
    
    for t_itr in range(t):
        n = int(input().strip())
        decentNumber(n)
        print("".join(map(str, decentNumber(n))))
