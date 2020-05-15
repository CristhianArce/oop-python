import math
import os
import random
import re
import sys

# Complete the compareTriplets function below.
def compareTriplets(a, b):
    alice_points=0
    bob_points=0
    for i in range(0,len(a)):
        if(a[i]!=b[i]):
            if(a[i]>b[i]):
                alice_points+=1
            else:
                bob_points+=1
    score=[]
    score.append(alice_points)
    score.append(bob_points)
    return score

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
