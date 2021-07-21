'''
CSC 506 - Critical Thinking 3
Karl Estes
Created Thursday, June 24th, 2021
Due Sunday, June 27th, 2021

'''
from typing import List
import numpy as np
from numpy.core.fromnumeric import sort
from numpy.core.numeric import array_equal
from numpy.lib.function_base import append
from numpy.random import rand
import pandas as pd
import math
from time import sleep, time
from os import system, name

RED = "\u001b[38;5;196m"
YELLOW = "\u001b[38;5;226m"
GREEN = "\u001b[38;5;34m"
ORANGE = "\u001b[38;5;209m"
PURPLE = "\u001b[38;5;165m"
BOLD = "\u001b[38;5;15m"
RESET = "\u001b[0m"

def clearTerminal():
    """Clears the terminal of all text on Windows/MacOs/Linux"""
    
    # For windows
    if name == 'nt':
        _ = system('cls')
    # Mac and linux 
    else:
        _ = system('clear')

def round_dec(num, places = 9):
    """Rounds the provided number to a specific number of decimal places (defaulted to 2)"""

    multiplier = 10 ** places

    return math.trunc(num * multiplier) / multiplier

class Sort():
    """
    The sort object contains all of the sorting functions necessary for comparison in 
    CSC 506 Critical Thinking 3. Each of these sorting algorithms should sort an array
    into ascending order.
    """

    def run_all(self, arr, hybrid_quicksort_threshold=10, print_msg=True):
        """
        Runs all of the sorting functions on the given array.

        A copy of the array will be made before each sorting function is run, and a sorted copied will be generated
        before the tests so a comparison can be made to ensure the array is properly sorted by each algorithm.

        Parameters
        ----------
        arr : []
            The array that will be sorted by each sorting function

        hybrid_quicksort_threshold : int
            The size threshold for the hybrid quicksort algorithm that determines when insertion sort will be used versus a quicksort recursive call.
            10 was arbitrarily chosen based off of numerous examples seen on coding tutorial websites

        Return
        ----------
        times -> List of runtimes for the algorithm in the following order
            * Selection Sort
            * Insertion Sort
            * Shell Sort
            * Quick Sort
            * Hybrid Quick Sort
            * Merge Sort
            * Radix Sort
        """

        times = []

        # Create the sorted array
        if print_msg:
            print("\nGenerating a sorted array for comparisons with Numpy's included sort function")
        sorted_arr = np.sort(np.copy(arr))

        # ***** Run all of the tests *****
        
        # Selection Sort
        if print_msg:
            print("\nRunning timed test of the " + ORANGE +  "Selection Sort" + RESET + " Algorithm")
        arr_copy = np.copy(arr)
        start = time()
        self.selection_sort(arr_copy, 0, len(arr_copy)-1)
        end = time()
        times.append(end-start)
        if print_msg:
            print("Runtime for " + ORANGE + "Selection Sort " + RESET + "was " + BOLD + f"{round_dec((end-start))} seconds" + RESET)

        if print_msg:
            if np.array_equal(sorted_arr, arr_copy):
                print("Verification of Sort: " + GREEN + "Successfull!" + RESET)
            else:
                print("Verification of Sort: " + RED + "Failed!" + RESET)
                print("Original  : {}".format(arr))
                print("Pre-Sorted: {}".format(sorted_arr))
                print("Algorithm : {}".format(arr_copy)) 

        # Insertion Sort
        if print_msg:
            print("\nRunning timed test of the " + ORANGE +  "Insertion Sort" + RESET + " Algorithm")
        arr_copy = np.copy(arr)
        start = time()
        self.insertion_sort(arr_copy, 0, len(arr_copy)-1)
        end = time()
        times.append(end-start)
        if print_msg:
            print("Runtime for " + ORANGE + "Insertion Sort " + RESET + "was " + BOLD + f"{round_dec((end-start))} seconds" + RESET)

        if print_msg:
            if np.array_equal(sorted_arr, arr_copy):
                print("Verification of Sort: " + GREEN + "Successfull!" + RESET)
            else:
                print("Verification of Sort: " + RED + "Failed!" + RESET)
                print("Original  : {}".format(arr))
                print("Pre-Sorted: {}".format(sorted_arr))
                print("Algorithm : {}".format(arr_copy)) 

        # Shell Sort
        if print_msg:
            print("\nRunning timed test of the " + ORANGE +  "Shell Sort" + RESET + " Algorithm")
        arr_copy = np.copy(arr)
        start = time()
        self.shell_sort(arr_copy)
        end = time()
        times.append(end-start)
        if print_msg:
            print("Runtime for " + ORANGE + "Shell Sort " + RESET + "was " + BOLD + f"{round_dec((end-start))} seconds" + RESET)

        if print_msg:
            if np.array_equal(sorted_arr, arr_copy):
                print("Verification of Sort: " + GREEN + "Successfull!" + RESET)
            else:
                print("Verification of Sort: " + RED + "Failed!" + RESET)
                print("Original  : {}".format(arr))
                print("Pre-Sorted: {}".format(sorted_arr))
                print("Algorithm : {}".format(arr_copy)) 

        # Quick Sort
        if print_msg:
            print("\nRunning timed test of the " + ORANGE +  "Quick Sort" + RESET + " Algorithm")
        arr_copy = np.copy(arr)
        start = time()
        self.quicksort(arr_copy, 0, len(arr_copy)-1)
        end = time()
        times.append(end-start)
        if print_msg:
            print("Runtime for " + ORANGE + "Quick Sort " + RESET + "was " + BOLD + f"{round_dec((end-start))} seconds" + RESET)

        if print_msg:
            if np.array_equal(sorted_arr, arr_copy):
                print("Verification of Sort: " + GREEN + "Successfull!" + RESET)
            else:
                print("Verification of Sort: " + RED + "Failed!" + RESET)
                print("Original  : {}".format(arr))
                print("Pre-Sorted: {}".format(sorted_arr))
                print("Algorithm : {}".format(arr_copy)) 

        # Hybrid Quick Sort
        if print_msg:
            print("\nRunning timed test of the " + ORANGE +  "Hybrid Quick Sort" + RESET + " Algorithm")
        arr_copy = np.copy(arr)
        start = time()
        self.hybrid_quicksort(arr_copy, 0, len(arr_copy)-1, hybrid_quicksort_threshold)
        end = time()
        times.append(end-start)
        if print_msg:
            print("Runtime for " + ORANGE + "Hybrid Quick Sort " + RESET + "was " + BOLD + f"{round_dec((end-start))} seconds" + RESET)

        if print_msg:
            if np.array_equal(sorted_arr, arr_copy):
                print("Verification of Sort: " + GREEN + "Successfull!" + RESET)
            else:
                print("Verification of Sort: " + RED + "Failed!" + RESET)
                print("Original  : {}".format(arr))
                print("Pre-Sorted: {}".format(sorted_arr))
                print("Algorithm : {}".format(arr_copy)) 

        # Merge Sort
        if print_msg:
            print("\nRunning timed test of the " + ORANGE +  "Merge Sort" + RESET + " Algorithm")
        arr_copy_merge = np.copy(arr)
        start = time()
        #self.merge_sort(arr_copy, 0, len(arr_copy)-1)
        self.merge_sort(arr_copy_merge)
        end = time()
        times.append(end-start)
        if print_msg:
            print("Runtime for " + ORANGE + "Merge Sort " + RESET + "was " + BOLD + f"{round_dec((end-start))} seconds" + RESET)

        if print_msg:
            if np.array_equal(sorted_arr, arr_copy_merge):
                print("Verification of Sort: " + GREEN + "Successfull!" + RESET)
            else:
                print("Verification of Sort: " + RED + "Failed!" + RESET)
                print("Original  : {}".format(arr))
                print("Pre-Sorted: {}".format(sorted_arr))
                print("Algorithm : {}".format(arr_copy_merge)) 

        # Radix Sort
        if print_msg:
            print("\nRunning timed test of the " + ORANGE +  "Radix Sort " + RESET + "Algorithm")
        arr_copy = np.copy(arr)
        start = time()
        self.radix_sort(arr_copy)
        end = time()
        times.append(end-start)
        if print_msg:
            print("Runtime for " + ORANGE + "Radix Sort " + RESET + "was " + BOLD + f"{round_dec((end-start))} seconds" + RESET)

        if print_msg:
            if np.array_equal(sorted_arr, arr_copy):
                print("Verification of Sort: " + GREEN + "Successfull!" + RESET)
            else:
                print("Verification of Sort: " + RED + "Failed!" + RESET)
                print("Original  : {}".format(arr))
                print("Pre-Sorted: {}".format(sorted_arr))
                print("Algorithm : {}".format(arr_copy)) 

        return times

    def radix_sort(self, arr):
        """Performs radix sort on the passed array. The array should be of integer values"""

        # Create buckets
        buckets = [[] for x in range(10)]

        # Find the max length in number of digits
        max_digits = self._radix_get_length(max(arr))


        pow10 = 1

        for digits in range(0, max_digits):
            for i in range(len(arr)):
                
                # Calculate bucket index
                bucket_index = abs(arr[i] // pow10) % 10
                
                # Add to array
                buckets[bucket_index].append(arr[i])
            
            
            # Place everything from the buckets back into the array
            index = 0
            for i in range(10):
                for j in range(len(buckets[i])):
                    arr[index] = buckets[i][j]
                    index += 1
            
            # Move to next power of 10
            pow10 = 10 * pow10
            
            # Clear all the buckets
            for x in range(10):
                buckets[x].clear()
                           
    def _radix_get_length(self, value) -> int:
        """Returns the number of places (digits) in the passed value"""

        if value == 0:
            return 1
            
        digits = 0

        while value != 0:
            digits += 1
            value = value // 10
            
        return digits

    def shell_sort(self, arr):
        '''
        Shell sort is a modification of insertion sort where we begin by swapping
        values as needed that are at a gap of h apart. This continues until a gap 
        value of one is reached and "insertion sort" has run on the entire array
        
        Some potential gap generation algorithms are discussed here:
        https://en.wikipedia.org/wiki/Shellsort
        '''
        
        # Generate the gaps
        gaps = self._calc_gaps(len(arr))

        # This algorithm is Marcin Ciura's gap sequence with an inner insertion sort
        for gap in gaps:

            for i in range(gap, len(arr)):
                temp = arr[i]

                j = i

                while j >= gap and arr[j-gap] > temp:
                    arr[j] = arr[j-gap]
                    j -= gap
                
                arr[j] = temp       
        
    def _calc_gaps(self, arr_len):
        '''
        The following uses Sedgewicks proposed algorithm for calculating gap
        intervals to give a worse-case O(N ^ (4/3))
        
        This algorithm does work best on array's of size > 4000
        
        Reference: https://oeis.org/A033622
        '''
        
        gaps = []
        
        # Continue to loop until all gap values have been generated
        # The generation should stop when the generated gap value exceeds
        # the length of the array
        for k in range(0, arr_len):
            
            # Even and odd k-values have different gap generations
            if k % 2 == 0:
                new_gap = 9 * ((2 ** k) - (2 ** (k/2))) + 1
            else:
                new_gap = (8 * (2 ** k)) - (6 * (2 ** ((k + 1) / 2))) + 1
                
            if new_gap > arr_len:
                break
                
            #gaps.append(int(new_gap))
            gaps.insert(0, int(new_gap))
            
        return gaps

        '''
        Merges the two array halves generated by the merge_sort function
        '''
        
        # Create two temporary subarrays
        L = np.copy(arr[:m])
        R = np.copy(arr[m:])
        
        i = j = k = 0
        
        # Copy data from temp arrays back to main array
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
            
        # Copy over any remaining elements
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

    def merge_sort(self, arr):
        """Algorithm was based off of Mayank Khanna's contribution on https://www.geeksforgeeks.org/merge-sort/"""
        if len(arr) > 1:
    
            # Finding the mid of the array
            mid = len(arr)//2
    
            # Dividing the array elements
            L = np.copy(arr[:mid])
    
            # into 2 halves
            R = np.copy(arr[mid:])
    
            # Sorting the first half
            self.merge_sort(L)
    
            # Sorting the second half
            self.merge_sort(R)
    
            i = j = k = 0
    
            # Copy data to temp arrays L[] and R[]
            while i < len(L) and j < len(R):
                if L[i] < R[j]:
                    arr[k] = L[i]
                    i += 1
                else:
                    arr[k] = R[j]
                    j += 1
                k += 1
    
            # Checking if any element was left
            while i < len(L):
                arr[k] = L[i]
                i += 1
                k += 1
    
            while j < len(R):
                arr[k] = R[j]
                j += 1
                k += 1

    def selection_sort(self, arr, l, r):

        # Begin at beginning of array and on each pass select the smallest element
        # and move it into place
        for i in range(l, r):
        
            smallest = i
            
            for j in range (i+1, r+1):
            
                # Set smallest index if new smallest number was fonud    
                if arr[j] < arr[smallest]:
                    smallest = j 
            
            # Swap the smallest value into place
            arr[i], arr[smallest] = arr[smallest], arr[i]

    def quicksort(self, array, left, right):

        # Recursive base case
        if right - left <= 0:
            return

        # Find the next pivot point
        partition_index = self._quicksort_partition(array, left, right)

        # Recursively sort left half of pivot
        self.quicksort(array, left, partition_index - 1)

        # Recursively sort right half of pivot
        self.quicksort(array, partition_index + 1, right)

    def _quicksort_partition(self, array, left, right) -> int:

        pivot = array[right]
        i = j = left

        for i in range(left, right):
            if array[i] < pivot:
                array[i], array[j] = array[j], array[i]
                j+= 1

        array[j], array[right] = array[right], array[j]
        return j

    def hybrid_quicksort(self, array, left, right, threshold):

        # Base case

        # Recursive base case
        if right - left <= 0:
            return

        if (right-left + 1) <= threshold:
            self.insertion_sort(array,left,right)
            return

        # Find the next pivot point
        partition_index = self._quicksort_partition(array, left, right)

        # Recursively sort left half of pivot
        self.quicksort(array, left, partition_index - 1)

        # Recursively sort right half of pivot
        self.quicksort(array, partition_index + 1, right)

    def insertion_sort(self, arr, l, r):

        for i in range(r-l+1):

            # First element is always sorted
            if i == 0:
                continue

            # Select the value to be inserted
            value = arr[i]
            j = i

            # Locate location in array to insert element
            while j > 0 and arr[j-1] > value:

                # Move the element over
                arr[j] = arr[j-1]
                j -= 1
            
            # Insert the value to proper location in array
            arr[j] = value

if __name__ == "__main__":

    clearTerminal()

    print(BOLD + "****** CSC 506 - Critical Thinking 3 ******")
    print("   *** Sorting Algorithm Comparisons ***")
    print("-------------------------------------------\n" + RESET)

    sorter = Sort()
    results = []
    averages = np.array([[]])

    # Loop through all Iterations
    for test_number in range(3):

        # Generate random array
        randarr = np.random.randint(0, 10000, 5000)

        for count in range (100):
            print(ORANGE + "\n----- Running Test {} - Iteration {} -----".format(test_number+1, count+1) + RESET)

            # Tests functions and append runtime data
            times = sorter.run_all(randarr,hybrid_quicksort_threshold=10,print_msg=False)

            results.append(times)
            
        if np.size(averages, axis=1) == 0:
            averages = np.array([np.mean(results,axis=0)])
        else:
            averages = np.append(averages, [np.mean(results,axis=0)], axis=0)
        results.clear()
        

    print(averages*(10**3))
    # Save Data
    pd.DataFrame(averages,columns=["Selection", "Insertion", "Shell", "Quick", "Hybrid Quick", "Merge", "Radix"]).to_csv("results_5000.csv")

    # Visualize?
    