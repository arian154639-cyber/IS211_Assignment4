"""
I tried to keep the provided skeleton as intact as possible.
"""

import time
import random


def get_me_random_list(n):
    """Generate list of n elements in random order
    
    :params: n: Number of elements in the list
    :returns: A list with n elements in random order
    """
    a_list = list(range(n))
    random.shuffle(a_list)
    return a_list


def sequential_search(a_list, item):
    pos = 0
    found = False

    while pos < len(a_list) and not found:
        if a_list[pos] == item:
            found = True
        else:
            pos = pos + 1

    return found


def ordered_sequential_search(a_list, item):
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

    return found


def binary_search_iterative(a_list,item):
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

    return found
    
    
def binary_search_recursive(a_list,item):
    if len(a_list) == 0:
        return False
    else:
        midpoint = len(a_list) // 2
        if a_list[midpoint] == item:
            return True
        else:
            if item < a_list[midpoint]:
                return binary_search_recursive(a_list[:midpoint], item)
            else:
                return binary_search_recursive(a_list[midpoint + 1:], item)


if __name__ == "__main__":
    """Main entry point"""
    list_sizes = [500, 1000, 5000]

    for the_size in list_sizes:
        total_time_seq = 0
        for i in range(100):
            mylist = get_me_random_list(the_size)
            # sorting is not needed for sequential search.
            start = time.time()
            check = sequential_search(mylist, 99999999)
            time_spent = time.time() - start
            total_time_seq += time_spent
        
        avg_seq = total_time_seq / 100
        print(f"Sequential Search took {avg_seq:10.7f} seconds to run, on average for a list of {the_size} elements")

        total_time_ord_seq = 0
        for i in range(100):
            mylist = get_me_random_list(the_size)
            mylist = sorted(mylist)
            start = time.time()
            check = ordered_sequential_search(mylist, 99999999)
            time_spent = time.time() - start
            total_time_ord_seq += time_spent
        
        avg_ord_seq = total_time_ord_seq / 100
        print(f"Ordered Sequential Search took {avg_ord_seq:10.7f} seconds to run, on average for a list of {the_size} elements")

        total_time_bin_iter = 0
        for i in range(100):
            mylist = get_me_random_list(the_size)
            mylist = sorted(mylist)
            start = time.time()
            check = binary_search_iterative(mylist, 99999999)
            time_spent = time.time() - start
            total_time_bin_iter += time_spent
        
        avg_bin_iter = total_time_bin_iter / 100
        print(f"Binary Search Iterative took {avg_bin_iter:10.7f} seconds to run, on average for a list of {the_size} elements")

        total_time_bin_rec = 0
        for i in range(100):
            mylist = get_me_random_list(the_size)
            mylist = sorted(mylist)
            start = time.time()
            check = binary_search_recursive(mylist, 99999999)
            time_spent = time.time() - start
            total_time_bin_rec += time_spent
        
        avg_bin_rec = total_time_bin_rec / 100
        print(f"Binary Search Recursive took {avg_bin_rec:10.7f} seconds to run, on average for a list of {the_size} elements")