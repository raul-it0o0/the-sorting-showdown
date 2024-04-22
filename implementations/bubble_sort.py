import time
import random

import sys

def generate_random(amount,min_bytes,max_bytes):
    min_value = 2**(min_bytes*8)
    max_value = 2**(max_bytes*8)

    return [random.randrange(min_value,max_value) for _ in range(amount)]

def bubble_sort(arr):
    
    n = len(arr)

    for i in range(n):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    
    return arr

def main():
    print(sys.getrecursionlimit())

if __name__ == '__main__':
    main()