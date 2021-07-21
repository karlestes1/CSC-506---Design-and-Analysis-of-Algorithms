# CSC506 Critical Thinking 1 Option 2
# Created by Karl Estes
# Created: Thursday, June 10, 2021

# Below are solutions to the following problem: When given an arrangement of the digits 0,1,2,3,4,5,6,7,8,9
# rearrange the digits so that the new arrangement represents the next larger value that can be represented by
# these digits (or report that no such rearrangement exists if a larger value cannot be produced)

import os
import sys
import numpy as np
from collections import Counter
import time
import copy
import pandas as pd
from pandas.core.frame import DataFrame

def convert_array_to_int(num_array):
    '''
    Takes an array of single digit integers (0 <= arr[i] <= 9) and converts it into
    a single integer value. Returns the calculated result
    '''
    x = 0

    for i in range(0, len(num_array)):
        x = x*10 + num_array[i]

    return x

def brute_force(num_array):
    '''
    The following is a brute force approach to solving the outlined problem. Assuming one started with 
    those outlined digits, one could increment the overall number by 1 and check if it was a new permutation
    of the provided digits.

    While not technically a rearrangement, it would discover all possible arrangements between the provided
    starting point and an ending point. The end point would be all the digits in descending order since no
    possible arrangement after that could be larger
    
    Returns a list of all calculated permutations
    '''

    permutations = []
    sorted_array = sorted(num_array, reverse=True)
    start = time.time()

    # Add the initial array to the permutation list
    permutations.append(num_array)

    while True:

        current = time.time()

        print_runtime(start, current)

        # Check if end case
        if np.array_equal(num_array, sorted_array):
            break

        if Counter(num_array) == Counter(sorted_array):
            permutations.append(convert_array_to_int(num_array))
       
        # Increment array by one
        i = len(num_array) - 1

        while num_array[i] == 9:
            num_array[i] = 0
            i -= 1

        num_array[i] += 1

        
    return permutations


def find_increasing_permutations(num_array):
    '''
    The following is a refined algorithm for calculating the permutations of an array of digits.
    
    While the brute force approach adopted a lengthy increment by 1 and check approach, the following
    algorithm traverses the array and rearranges the existing digits in place to create the next largest
    possible permutation. 
    
    Returns a list of all calculated permutations
    '''
    n = len(num_array)
    m = n-1
    permutations = []
    start = time.time()

    # Add initial state to permutation list
    permutations.append(convert_array_to_int(num_array))

    # Loop until no more permutations of increasing value can be made
    while m > 0:

        current = time.time()

        print_runtime(start, current)

        # Check if at swap point
        if num_array[m-1] < num_array[m]:
            s = m

            # Find swap value
            for j in range(m+1, n):

                # Check is smaller larger value
                if num_array[j] > num_array[m-1] and num_array[j] < num_array[s]:
                    s = j

            # Swap the values
            num_array[m-1], num_array[s] = num_array[s], num_array[m-1]

            # Sort array from m to the end
            num_array[m:] = sorted(num_array[m:])

            # Append new number to permutations
            permutations.append(convert_array_to_int(num_array))

            # Reset m so on decrement if restarts at last index in array
            m = n

        m -= 1

    # print("No more possible permutations")

    return permutations

def run(arr):
	
    print(f"**** Array: {arr} ****")
	
    
    start_brute = time.time()
    results_brute = brute_force(copy.deepcopy(arr))
    end_brute = time.time()
	

    start_refined = time.time()
    results_refined = find_increasing_permutations(copy.deepcopy(arr))
    end_refined = time.time()

    time_brute = end_brute - start_brute
    time_refined = end_refined - start_refined

    # print("Brute Force Approach")
    # print(f"# of permutations = {len(results_brute)}")
    # print(f"Runtime = {time_brute} s\n")

    brute = {'Array': copy.deepcopy(arr), 'Time': time_brute, 'Permutation Count': len(results_brute)}
    

    # print("Refined Approach")
    # print(f"# of permutations = {len(results_refined)}")
    # print(f"Runtime = {time_refined} s\n")

    refined = {'Array': copy.deepcopy(arr), 'Time': time_refined, 'Permutation Count': len(results_refined)}

    df = pd.DataFrame(data=[brute,refined],index=["Brute", "Refined"])
    # df = pd.DataFrame(data=[refined],index=["Refined"])
    
    return df

def print_runtime(start_time, current_time):
    print(f"Current Runtime: {round((current_time - start_time), 3)}", end="\r")


def main():

    # Change the directory to that of the 
    os.chdir(os.path.dirname(sys.argv[0]))

    digits = []
    df = DataFrame()

    # Will test growing array with digits 0 ... 5
    for i in range(10):

        digits.append(i)

        # Run each array permutation check 10 times
        for j in range(1):
            print(f"\nArray size: {i + 1} | Iteration {j+1}")
            df = df.append(run(digits))

    print(df)

    # Save results to csv
    df.to_csv("full_run.csv")

# TODO - seaborn? mathplotlib? Data visualization of time it took?

if __name__ == "__main__":
    main()





