import math
import os
import random
import re
import sys

# Complete the staircase function below.
def staircase(n):
    string_builder=""
    for i in range (1,n+1):
        espacios = n-i
        string_builder+=" "*espacios+"#"*i+"\n"
    print(string_builder)

if __name__ == '__main__':
    n = int(input())

    staircase(n)
