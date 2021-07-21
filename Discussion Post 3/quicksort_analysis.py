import funcs as fc
import random
def quicksort(array, left, right):

    # Recursive base case
    if right - left <= 0:
        return

    # Find the next pivot point
    partition_index = quicksort_partition(array, left, right)

    # Recursively sort left half of pivot
    quicksort(array, left, partition_index - 1)

    # Recursively sort right half of pivot
    quicksort(array, partition_index + 1, right)

def quicksort_partition(array, left, right):

    pivot = array[right]

    # Set left and right indices
    l_index = left
    r_index = right - 1

    # Loop until return condition met
    while True:

        # Increment left index until value greater than pivot found
        while array[l_index] < pivot:
            l_index += 1

        # Decrement right index until value less than pivot found
        while r_index > 0 and array[r_index] > pivot :
            r_index -= 1
        
        # If indices match or have passed each other, break the loop
        if l_index >= r_index:
            break
        # Otherwise, swap the values 
        else:
            array[l_index], array[r_index] = array[r_index], array[l_index]
            l_index += 1

    # Put the pivot point into place
    array[l_index], array[right] = array[right], array[l_index]

    # Return index of where pivot was placed
    return l_index

def hybrid_quicksort(array, left, right, threshold):

    # Base case
    if left >= right:
        return

    if (right - left + 1) < threshold:
        insertion_sort(array, left, right)
    else:
        # Partition the arrays
        partition_index = quicksort_partition(array, left, right)

        # Recursive call on each left & right partition
        hybrid_quicksort(array, left, partition_index-1, threshold)
        hybrid_quicksort(array, partition_index+1, right, threshold)

def insertion_sort(array, l, r):

    for i in range(r-l+1):

        # First element is always sorted
        if i == 0:
            continue

        # Select the value to be inserted
        value = array[i]
        j = i

        # Locate location in array to insert element
        while j > 0 and array[j-1] > value:

            # Move the element over
            array[j] = array[j-1]
            j -= 1
        
        # Insert the value to proper location in array
        array[j] = value

qs_run = fc.Runtime(print=False)
hqs_run = fc.Runtime(print=False)

arr1_1 = [2,7,0,-2,4,-5,7,12,7]
arr2_1 = [-4,-9,2,4,-6,14,867,124,-432,4]
arr3_1 = [4,456,1234,1123,5,-7,-8647,-6,123,7,6,1,245,5432,2143,6,76,34,234,623,2345,2,-2536,1245,-26542,-6,-1234,-652,245,154,5,6543,7,34657,2345,134,65,76,3256,234,-265,-52346,-734,2345,-67537,24,-2]

arr1_2 = [2,7,0,-2,4,-5,7,12,7]
arr2_2 = [-4,-9,2,4,-6,14,867,124,-432,4]
arr3_2 = [4,456,1234,1123,5,-7,-8647,-6,123,7,6,1,245,5432,2143,6,76,34,234,623,2345,2,-2536,1245,-26542,-6,-1234,-652,245,154,5,6543,7,34657,2345,134,65,76,3256,234,-265,-52346,-734,2345,-67537,24,-2]



print("\nArray: {}".format(arr1_1))

qs_run.start()
quicksort(arr1_1,0,len(arr1_1)-1)
qs_run.stop()

hqs_run.start()
hybrid_quicksort(arr1_2,0,len(arr1_2)-1, 4)
hqs_run.stop()

print("Sorted: {}".format(arr1_1))
print("Quicksort Runtime        : {} us".format(fc.round_dec(qs_run.elapsed_time * (10 ** 6), 3)))
print("Hybrid Quicksort Runtime : {} us".format(fc.round_dec(hqs_run.elapsed_time * (10 ** 6), 3)))


print("\nArray: {}".format(arr2_1))

qs_run.start()
quicksort(arr2_1,0,len(arr2_1)-1)
qs_run.stop()

hqs_run.start()
hybrid_quicksort(arr2_2,0,len(arr2_2)-1, 4)
hqs_run.stop()

print("Sorted: {}".format(arr2_1))
print("Quicksort Runtime        : {} us".format(fc.round_dec(qs_run.elapsed_time * (10 ** 6), 3)))
print("Hybrid Quicksort Runtime : {} us".format(fc.round_dec(hqs_run.elapsed_time * (10 ** 6), 3)))


print("\nArray: {}".format(arr3_1))

qs_run.start()
quicksort(arr3_1,0,len(arr3_1)-1)
qs_run.stop()

hqs_run.start()
hybrid_quicksort(arr3_2,0,len(arr3_2)-1, 4)
hqs_run.stop()

print("Sorted: {}".format(arr3_1))
print("Quicksort Runtime        : {} us".format(fc.round_dec(qs_run.elapsed_time * (10 ** 6), 3)))
print("Hybrid Quicksort Runtime : {} us".format(fc.round_dec(hqs_run.elapsed_time * (10 ** 6), 3)))





