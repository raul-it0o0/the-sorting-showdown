import time
import random

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