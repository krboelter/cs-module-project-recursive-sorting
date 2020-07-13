# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements

    # Your code here
    
    merged_arr = merge_sort(arrA) + merge_sort(arrB)

    return merged_arr

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    # Your code here

    # if the array only has 1 element, return the array
    if len(arr) <= 1:
        return arr

    pivot = arr[0]
    left = []
    right = []

    for i in arr[1:]:
        if i > pivot:
            right.append(i)
        else:
            left.append(i)

    left.append(pivot)
    arr = merge(left, right)

    return arr

# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
def merge_in_place(arr, start, mid, end):
    # Your code here
    pass


def merge_sort_in_place(arr, l, r):
    # Your code here
    pass

