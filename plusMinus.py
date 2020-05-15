import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    zeros=0
    positives=0
    negatives=0
    total = len(arr)
    for i in arr:
        if(i>0):
            positives+=1
        elif(i<0):
            negatives+=1
        else:
            zeros+=1
    zeros=zeros/total
    positives=positives/total
    negatives=negatives/total
    print('{:6.6f}'.format(positives))
    print('{:6.6f}'.format(negatives))
    print('{:6.6f}'.format(zeros))

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
