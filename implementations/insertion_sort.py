import random
import time

def generate_random(amount,min_bytes,max_bytes):
    min_value = 2**(min_bytes*8)
    max_value = 2**(max_bytes*8)

    return [random.randrange(min_value,max_value) for _ in range(amount)]

def insertion_sort(arr):
    
    n = len(arr)

    for i in range(1,n):
        aux = arr[i]
        j = i-1
        while j >= 0 and arr[j] > aux:
            arr[j+1] = arr[j]
            j = j-1
        arr[j+1] = aux
    
    return arr

def main():
    sum = 0
    for i in range(3):
        l = generate_random(75000,0,1)
        l_sorted = sorted(l)
        time_start = time.perf_counter()
        l = insertion_sort(l)
        time_end = time.perf_counter()
        assert l_sorted == l
        exec_time = time_end - time_start
        print(f'Execution time: {time_end - time_start}\n')
        sum += exec_time
    print(f'Average of 3 tests: {sum / 3}\n')

if __name__ == '__main__':
    main()