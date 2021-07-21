
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
        hybrid_quicksort(array, left, partition_index-1)
        hybrid_quicksort(array, right, hybrid_quicksort+1)

def quicksort_partition(array, left, right):

    # Make the right most value the pivot value
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

    # Put the pivot point into place
    array[l_index], array[right] = array[right], array[l_index]

    # Return index of where pivot was placed
    return l_index

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