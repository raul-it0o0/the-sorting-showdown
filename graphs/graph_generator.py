import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl
import csv

fig, ax = plt.subplots(figsize=(7,3), layout='constrained')
plt.rcParams['text.usetex'] = True
plt.ticklabel_format(style = 'plain')

label_color_scheme = {'random':'Random',
                 'sorted':'Sorted',
                 'reverse_sorted':'Reverse Sorted',
                 'flat_list':'Flat List'}

# Form problem size list

with open(r'U:\MPI\Activity 1\experiment_data\results_bubble_sort.csv','r') as fin:

    current_sorting_config = None

    used_input_sizes = []

    reader = csv.reader(fin)

    next(reader) # skip header row

    for line in reader:

        if line[1] != current_sorting_config:
            if current_sorting_config != None:
                ax.plot(current_sorting_config_results.keys(),
                          current_sorting_config_results.values(),
                          label=label_color_scheme[current_sorting_config][0])
        
            current_sorting_config = line[1]

            current_sorting_config_results = {}

        current_sorting_config_results[int(line[0])] = float(line[3])
    
    ax.plot(current_sorting_config_results.keys(),
                          current_sorting_config_results.values(),
                          label=label_color_scheme[current_sorting_config][0])

ax.set_xlabel('Input array size (number of elements)')
ax.set_ylabel('Execution time ($s$)')
ax.set_title('Bubble Sort Execution Times')
ax.grid('True')
ax.legend(loc='upper left')

plt.show()

        
        
        
            

        



