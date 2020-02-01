def merge( arrA, arrB ):

    elements = len( arrA ) + len( arrB ) #Get the total number of elements
    
    merged_arr = [0] * elements # reate an empty list based on the size of elements
    
    #Initialize reference points to keep track of increments
    a = 0
    b = 0

    # Go through the list and replace the 0's in merged_arr with the smallest element between arrA and arrB
    for index in range(elements):
        # Checks to see if the list is done sorting on side A and assigns the current index to the value of arrB[b]
        if a >= len(arrA):
            merged_arr[index] = arrB[b]
            b += 1
        # Checks to see if the list is done sorting on side B and assigns the current index to the value of arrA[a]
        elif b >= len(arrB):
            merged_arr[index] = arrA[a]
            a += 1
        # If the value of a is smaller, assign a to the merged_arr[index] and move on to its next reference point
        elif arrA[a] < arrB[b]:
            merged_arr[index] = arrA[a]
            a += 1
        # Otherwise, assign b to the merged_arr[index] and move on to its next reference point
        else:
            merged_arr[index] = arrB[b]
            b += 1

    # Returns the merged array
    return merged_arr

# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):   
    if len(arr) > 1:
        # Get the middle (floor division)
        middle = len(arr) // 2
        # Get everything from the LHS and break it down until you get a list of length 1
        left = merge_sort(arr[:middle])
        # Get everything from the LHS and break it down until you get a list of length 1
        right = merge_sort(arr[middle:])
        # Re-assign arr
        arr = merge(left, right)
    return arr

# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
