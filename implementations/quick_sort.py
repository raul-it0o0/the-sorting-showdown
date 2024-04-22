import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl
import list_generators 

import sys
sys.setrecursionlimit(100000)

# Quicksort
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
    
    fig, ax = plt.subplots(2,3, figsize=(15,6), layout='constrained')
    plt.rcParams['text.usetex'] = True
    
    problem_sizes = [100,500,5000,10000,25000,50000,75000,100000,500000,1000000]

    generate_graph_using_range('random_with_duplicates',ax[0][0],problem_sizes,0,1,ax[1][0])
    generate_graph_using_range('sorted',ax[0][0],problem_sizes[:6:],0,1)
    generate_graph_using_range('reverse_sorted',ax[0][0],problem_sizes[:6:],0,1)
    generate_graph_using_range('flat_list_not_shuffled',ax[0][0],problem_sizes[:6:],0,1)
    generate_graph_using_range('flat_list_shuffled',ax[0][0],problem_sizes[:6:],0,1)

    generate_graph_using_range('random_with_duplicates',ax[0][1],problem_sizes,1,2,ax[1][1])
    generate_graph_using_range('sorted',ax[0][1],problem_sizes[:6:],1,2)
    generate_graph_using_range('reverse_sorted',ax[0][1],problem_sizes[:6:],1,2)
    generate_graph_using_range('flat_list_not_shuffled',ax[0][1],problem_sizes[:6:],1,2)
    generate_graph_using_range('flat_list_shuffled',ax[0][1],problem_sizes[:6:],1,2)
    
    generate_graph_using_range('random_with_duplicates',ax[0][2],problem_sizes,2,4,ax[1][2])
    generate_graph_using_range('sorted',ax[0][2],problem_sizes[:6:],2,4)
    generate_graph_using_range('reverse_sorted',ax[0][2],problem_sizes[:6:],2,4)
    generate_graph_using_range('flat_list_not_shuffled',ax[0][2],problem_sizes[:6:],2,4)
    generate_graph_using_range('flat_list_shuffled',ax[0][2],problem_sizes[:6:],2,4)

    plt.show()

# def generate_graph_using_range(list_config,axis,problem_sizes,min_byte_size,max_byte_size,axis_secondary=None):
    
#     if min_byte_size != 0:
#         start_val = 2**(min_byte_size*8)
#     else:
#         start_val = 0
#     stop_val = 2**(max_byte_size*8)-1

#     exec_times = []

#     sum = 0 
#     # 3 tests per problem size and average computation, ensure accuracy and avoid experiment errors (unexpected values)

#     for problem_size in problem_sizes:
#         for _ in range(3):
#             l = list_generators.list_config_properties[list_config][0](problem_size,start_val,stop_val)
#             # generate_random(problem_size,start_val,stop_val)
#             # generate list to be sorted

#             l_sorted = sorted(l)
#             # for sorting assertion

#             time_start = time.perf_counter()
#             l = quick_sort(l,len(l)-1)
#             time_end = time.perf_counter()

#             assert l_sorted == l

#             exec_time = time_end - time_start
#             sum += exec_time
        
#         exec_times.append(sum/3)
#         print(f'Finished problem size {problem_size} for {list_config} values [{start_val},{stop_val}].')

#     print(f'Finished {list_config} graph for values [{start_val},{stop_val}].') 
#     # to ensure everything is going well (optional)

#     axis.set_xlabel('Number of elements to sort')
#     axis.set_ylabel('Execution time ($s$)')
#     axis.set_title(f'Values range [${start_val},{stop_val}$]')
#     axis.grid('True')

#     if axis_secondary != None:
#         axis_secondary.set_xlabel('Number of elements to sort')
#         axis_secondary.set_ylabel('Execution time ($s$)')
#         axis_secondary.grid('True')
#         axis_secondary.plot(problem_sizes,
#                             exec_times,
#                             color=list_config_properties[list_config][1],
#                             label=list_config_properties[list_config][2])

#     return axis.plot(problem_sizes,
#               exec_times,
#               color=list_config_properties[list_config][1],
#               label=list_config_properties[list_config][2])