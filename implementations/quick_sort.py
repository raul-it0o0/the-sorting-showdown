import time
import csv
import list_generators

test_num = 3

import sys
# Raising recursion limit to avoiding runtime errors
sys.setrecursionlimit(100000)

def quick_sort(arr, end, start=0):

    if start < end:

        pivot = partition(arr, start, end)
        quick_sort(arr, pivot - 1, start)
        quick_sort(arr, end, pivot + 1)
        
    return arr

def partition(arr, start, end):

    pivot = arr[end]
    i = start - 1

    for j in range(start,end):
        if arr[j] <= pivot:
            i = i+1
            arr[i], arr[j] = arr[j], arr[i]

    
    arr[i+1], arr[end] = arr[end], arr[i+1]

    return i+1

if __name__ == '__main__':
    
    problem_sizes = [100,500,5000,10000,25000,50000,75000,100000,500000,1000000,2000000,5000000,10000000]
    test_cases = {1:2**(8*2)}
    array_generation_commands = {'random':list_generators.generate_random,
                                 'sorted':list_generators.generate_random_sorted,
                                 'reverse_sorted':list_generators.generate_random_reverse_sorted,
                                 'flat_list':list_generators.generate_flat_list_shuffled}
    

    for test_case in test_cases:
        for sorting_config_id in array_generation_commands:

            sum = 0

            for problem_size in problem_sizes:

                if ((sum / test_num) > 30):
                    print(f'{sorting_config_id} with size {problem_size} took {sum / test_num} seconds. Continue? (Y/N)')
                    if input() == 'N':
                        break
                

                to_append = [problem_size, sorting_config_id]
                sum = 0

                for _ in range(test_num): 

                    array = array_generation_commands[sorting_config_id](problem_size,0,test_cases[test_case]+1)
                    
                    sorted_array = sorted(array)

                    # time measurement starts just before the sorting function call
                    time_start = time.perf_counter()
                    quick_sort(array,len(array)-1)
                    time_end = time.perf_counter()

                    # time measurement ends right after sorting function return
                        
                    # assert array equality to ensure sorting has gone correctly
                    assert array == sorted_array

                    execution_time = time_end - time_start
                    sum += execution_time

                with open(r'results_quicksort.csv','a',newline='') as fout:
                    
                    csv_writer = csv.writer(fout)
                    to_append.append('quicksort')
                    to_append.append(sum / test_num)

                    csv_writer.writerow(to_append)