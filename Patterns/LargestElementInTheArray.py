from sys import *
from collections import *
from math import *

def largestElement(arr: [], n: int) -> int:

    # Write your code from here.
    max=0
    for i in range(len(arr)):
        if arr[i]>max:
            max=arr[i]
    return max
