import time
import random
import logging

test_num = 3

def generate_random(amount,start_val,stop_val):
    return [random.randrange(start_val,stop_val) for _ in range(amount)]

def generate_random_unique(amount,start_val,stop_val):
    return random.sample(range(start_val,stop_val),amount)
    # Returns <amount> unique items from the list <range(min_value,max_value)>

def generate_random_sorted(amount,start_val,stop_val):
    
    l = generate_random(amount,start_val,stop_val)

    return sorted(l) 
    # Sorted using Python's built-in sorting method (TimSort)

def generate_random_reverse_sorted(amount,start_val,stop_val):
    return generate_random_sorted(amount,start_val,stop_val)[::-1]

def generate_flat_list(amount,start_val,stop_val):
    
    l = []

    while len(l) < amount:
        # Pick a random number from 1 to <amount - len(l)> 
        # and append a random number from values <start> to <stop>
        # that many times
        if amount-len(l) == 1:
            l.append(random.randrange(start_val,stop_val))
        else:
            append_n_times = random.randrange(1,amount-len(l))
            value_to_append = random.randrange(start_val,stop_val)
            for _ in range(append_n_times):
                l.append(value_to_append)

    return l

def generate_flat_list_shuffled(amount,start_val,stop_val):
    
    l = generate_flat_list(amount,start_val,stop_val)
    random.shuffle(l)

    return l

# Almost sorted: research https://stackoverflow.com/questions/19825758/algorithm-to-generate-a-nearly-sorted-or-k-sorted-list

# The below dictionary defines how each list 
# configuration is generated in the program and
#  how it looks in the final
# generated graph.
list_config_properties = {'random_with_duplicates':[generate_random,'#B71C1C','Random (with possible duplicates)'],
                        'random_unique':[generate_random_unique,'#880E4F','Random (strictly unique)'],
                        'sorted':[generate_random_sorted,'#7B1FA2','Sorted (with possible duplicates)'],
                        'reverse_sorted':[generate_random_reverse_sorted,'#0D47A1','Reverse sorted (with possible duplicates)'],
                        'flat_list_not_shuffled':[generate_flat_list,'#006064','Flat list (not shuffled)'],
                        'flat_list_shuffled':[generate_flat_list_shuffled,'#7D0552','Flat list (shuffled)']
                        }

# The below function is the function which combines
# list generation as well as graph creation

def generate_graph(function_call, list_config, axis, problem_sizes, byte_size, secondary_axis=None):

    # Set the range for the generated values by converting bytes into decimal values
    start_val = -2**(byte_size*8 - 1)
    stop_val = 2**(byte_size*8 - 1) - 1

    execution_times = []
    sum = 0

    for problem_size in problem_sizes:
        # Conduct <test_num> tests for each problem size,
        # avoid experiment errors and ensure accuracy.
        for _ in range(test_num):

            # 1. Call appropriate function to 
            # generate random list based on list_config parameter
            l = list_config_properties[list_config][0](problem_size,start_val,stop_val)

            # 2. Created sorted variant of generated list
            # and assert at end of sorting to ensure the list is actually sorted
            l_sorted = sorted(l)

            # 3. Call sorting function and measure time
            time_start = time.perf_counter()
            exec(function_call)
            # Function call
            time_end = time.perf_counter()
            
            # Assert sorting
            assert l == l_sorted

            execution_time = time_end - time_start
            sum += execution_time

        execution_times.append(sum / test_num)

    
    # Graph configuration
    axis.set_xlabel('Number of elements to sort')
    axis.set_ylabel('Execution time ($s$)')
    axis.set_title(f'Values range [${start_val},{stop_val}$]')
    axis.grid('True')

    # Primary plot
    axis.plot(problem_sizes,
              execution_times,
              color=list_config_properties[list_config][1],
              label=list_config_properties[list_config][2])
    
    axis.set_xlim(left=0)
    axis.set_ylim(bottom=0)
    axis.legend(loc='upper right')
    
    # Secondary plot (if given by user)
    if secondary_axis is not None:
        secondary_axis.set_xlabel('Number of elements to sort')
        secondary_axis.set_ylabel('Execution time ($s$)')
        secondary_axis.grid('True')

        secondary_axis.plot(problem_sizes,
                            execution_times,
                            color=list_config_properties[list_config][1],
                            label=list_config_properties[list_config][2])
    
        secondary_axis.set_xlim(left=0)
        secondary_axis.set_ylim(bottom=0)
        secondary_axis.legend(loc='upper right')
    
    return

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


