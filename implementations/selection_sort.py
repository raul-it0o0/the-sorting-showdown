import random
import time

def generate_random(amount,min_bytes,max_bytes):
    min_value = 2**(min_bytes*8)
    max_value = 2**(max_bytes*8)

    return [random.randrange(min_value,max_value) for _ in range(amount)]

def selection_sort(arr):
    
    n = len(arr)

    for i in range(n-1):
        min_index = i
        for j in range (i+1,n):
            if arr[j] < arr[min_index]:
                min_index = j
            
        if arr[i] > arr[min_index]:
            arr[i], arr[min_index] = arr[min_index], arr[i]
    
    return arr

def main():
    
    sum = 0
    for j in [100,500,5000,10000,25000,50000,75000,100000]:
        for i in range(3):
            l = generate_random(j,1,2)
            l_sorted = sorted(l)
            time_start = time.perf_counter()
            l = selection_sort(l)
            time_end = time.perf_counter()
            assert l_sorted == l
            exec_time = time_end - time_start
            sum += exec_time
        print(f'Average execution time for {j} elements: {sum / 3}')

if __name__ == '__main__':
    main()