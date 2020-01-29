# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # find next smallest element
        for j in range(cur_index, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j

        # swap
        temp = arr[smallest_index]
        arr[smallest_index] = arr[cur_index]
        arr[cur_index] = temp

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    swaps_happened = True #tests if we are swapping
    while swaps_happened:
        swaps_happened = False
        # Loop through your array
        for i in range(0, len(arr) - 1):
            # Compare each element to its neighbor on the right
            if arr[i] > arr[i+1]:
                # If element on the right is smaller, swap them
                arr[i], arr[i+1] = arr[i+1], arr[i]
                swaps_happened = True # Clearly a swap happened
        # If swaps_happened is true, while loop condition holds
    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr