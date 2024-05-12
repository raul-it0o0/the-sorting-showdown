import time
import csv
import list_generators

test_num = 3

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
                    insertion_sort(array)
                    time_end = time.perf_counter()

                    # time measurement ends right after sorting function return
                        
                    # assert array equality to ensure sorting has gone correctly
                    assert array == sorted_array

                    execution_time = time_end - time_start
                    sum += execution_time

                with open(r'results_insertion_sort.csv','a',newline='') as fout:
                    
                    csv_writer = csv.writer(fout)
                    to_append.append('insertion_sort')
                    to_append.append(sum / test_num)

                    csv_writer.writerow(to_append)