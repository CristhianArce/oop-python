import math
import os
import random
import re
import sys

def leftRotation(a,d):
    str_arr = ""
    for i in range(0,d):
        aux = a[0]
        a.pop(0)
        a.append(aux)
    
    for i in range(0,len(a)):
        str_arr += str(a[i])+" "
    return str_arr

if __name__ == '__main__':
    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = list(map(int, input().rstrip().split()))
    print(leftRotation(a,d))
