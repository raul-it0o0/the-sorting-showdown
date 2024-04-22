import random
import time

def generate_random(amount,min_bytes,max_bytes):
    min_value = 2**(min_bytes*8)
    max_value = 2**(max_bytes*8)

    return [random.randrange(min_value,max_value) for _ in range(amount)]

def merge_sort(arr):
    
    n = len(arr)

    if (n <= 1): # array can no longer be divided
        return
    
    mid_index = n // 2
    left = []
    right = []

    # split array
    for i in range(n):
        if(i<mid_index):
            left.append(arr[i])
        else:
            right.append(arr[i])

    merge_sort(left) # split left sub-array until one element is left
    merge_sort(right) # split right sub-array until one element is left
    merge(left,right,arr) # left and right both are one element arrays
    
    return arr

def merge(left,right,final):
    n_left = len(left)
    n_right = len(right)
    i, l, r = 0, 0, 0

    # Elements are compared as follows:
    # First element from left with first element from right
    # Whichever element is the smallest (considering we want to sort in descending order)
    # gets placed in the final merged array, and the next element in that element's sub-array
    # gets compared with the first element from the other sub-array.

    while l < n_left and r < n_right:
        if left[l] < right[r]: # descending order
            final[i] = left[l]
            i+=1
            l+=1
        else:
            final[i] = right[r]
            i+=1
            r+=1

    # In some cases, elements from either the left or 
    # right sub-arrays will be left unplaced
    # in the final array. We ensure they are all placed using while loops:
    while l < n_left:
        final[i] = left[l]
        i+=1
        l+=1
    while r < n_right:
        final[i] = right[r]
        i+=1
        r+=1

    # Each sub-array will be sorted before merging. Now it is a matter of merging the
    # sub-arrays so that they are in correct order.

def main():

    sum = 0
    for j in [100,500,5000,10000,25000,50000,75000,100000]:
        for i in range(3):
            l = generate_random(j,2,4)
            l_sorted = sorted(l)
            time_start = time.perf_counter()
            l = merge_sort(l)
            time_end = time.perf_counter()
            assert l_sorted == l
            exec_time = time_end - time_start
            sum += exec_time
        print(f'Average execution time for {j} elements: {sum / 3}')

if __name__ == '__main__':
    main()