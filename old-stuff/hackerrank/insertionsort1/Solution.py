#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the insertionSort1 function below.
def insertionSort1(n, arr):
    def print_arr():
        print(' '.join(map(str, arr)))
    x = arr[n-1]
    for i in range(n-1, 0, -1):
        if arr[i-1] < x:
            arr[i] = x
            print_arr()
            break
        else:
            arr[i] = arr[i-1]
            print_arr()
    if arr[0] > x:
        arr[0] = x
        print_arr()

n = 10
arr = [2, 3, 4, 5, 6, 7, 8, 9, 10, 1]
insertionSort1(n, arr)
