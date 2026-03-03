"""
I tried to keep the provided skeleton as intact as possible. I could have chosen
to reuse the lists for ordered sequential, binary iterative, and binary recursive, 
but I opted to instead generate a new list for each.
"""
import time
import random


def get_me_random_list(n):
    """Generate list of n elements in random order
    
    :params: n: Number of elements in the list
    :returns: A list with n elements in random order
    """
    a_list = list(range(1, n + 1))
    random.shuffle(a_list)
    return a_list


def sequential_search(a_list, item):
    start_time = time.time()
    pos = 0
    found = False

    while pos < len(a_list) and not found:
        if a_list[pos] == item:
            found = True
        else:
            pos = pos + 1
    time_passed = time.time() - start_time
    return found, time_passed


def ordered_sequential_search(a_list, item):
    start_time = time.time()
    pos = 0
    found = False
    stop = False
    while pos < len(a_list) and not found and not stop:
        if a_list[pos] == item:
            found = True
        else:
            if a_list[pos] > item:
                stop = True
            else:
                pos = pos + 1
    time_passed = time.time() - start_time
    return found, time_passed


def binary_search_iterative(a_list,item):
    start_time = time.time()
    first = 0

    last = len(a_list) - 1
    found = False
    while first <= last and not found:
        midpoint = (first + last) // 2
        if a_list[midpoint] == item:
            found = True
        else:
            if item < a_list[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1
    time_passed = time.time() - start_time
    return found, time_passed
    
    
def binary_search_recursive(a_list,item):
    start_time = time.time()
    if len(a_list) == 0:
        result = False
    else:
        midpoint = len(a_list) // 2
        if a_list[midpoint] == item:
            result = True
        else:
            if item < a_list[midpoint]:
                result, _ = binary_search_recursive(a_list[:midpoint], item)
            else:
                result, _ = binary_search_recursive(a_list[midpoint + 1:], item)
    time_passed = time.time() - start_time
    return result, time_passed

if __name__ == "__main__":
    """Main entry point"""
    list_sizes = [500, 1000, 5000]
    for the_size in list_sizes:
        total_time_seq = 0
        total_time_ord_seq = 0
        total_time_bin_iter = 0
        total_time_bin_rec = 0

        for i in range(100):
            mylist = get_me_random_list(the_size)
            # sorting is not needed for sequential search.
            result, passed_time = sequential_search(mylist, 99999999)
            total_time_seq += passed_time
            sorted_list = sorted(mylist) 
            result, passed_time = ordered_sequential_search(sorted_list, 99999999)
            total_time_ord_seq += passed_time    
            result, passed_time = binary_search_iterative(sorted_list, 99999999)
            total_time_bin_iter += passed_time       
            result, passed_time = binary_search_recursive(sorted_list, 99999999)
            total_time_bin_rec += passed_time
        avg_seq = total_time_seq / 100
        avg_ord_seq = total_time_ord_seq / 100
        avg_bin_iter = total_time_bin_iter / 100
        avg_bin_rec = total_time_bin_rec / 100
        print(f"Sequential Search took {avg_seq:10.7f} seconds to run, on average for a list of {the_size} elements")
        print(f"Ordered Sequential Search took {avg_ord_seq:10.7f} seconds to run, on average for a list of {the_size} elements")
        print(f"Binary Search Iterative took {avg_bin_iter:10.7f} seconds to run, on average for a list of {the_size} elements")
        print(f"Binary Search Recursive took {avg_bin_rec:10.7f} seconds to run, on average for a list of {the_size} elements")
        
