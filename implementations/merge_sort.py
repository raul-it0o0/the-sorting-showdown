import time
import csv
import list_generators

test_num = 3

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
                    merge_sort(array)
                    time_end = time.perf_counter()

                    # time measurement ends right after sorting function return
                        
                    # assert array equality to ensure sorting has gone correctly
                    assert array == sorted_array

                    execution_time = time_end - time_start
                    sum += execution_time

                with open(r'results_merge_sort.csv','a',newline='') as fout:
                    
                    csv_writer = csv.writer(fout)
                    to_append.append('merge_sort')
                    to_append.append(sum / test_num)

                    csv_writer.writerow(to_append)