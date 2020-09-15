def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
    countA = 0
    countB = 0
    # if((len(arrA) == 0)):
    #     return arrB
    # elif(len(arrB) == 0):
    #     return arrA
    for i in range(len(merged_arr)):
        print(i)
        print(f"countA: {countA}")
        print(f"countB: {countB}")
        print(merged_arr)
        if(countB >= len(arrB)):
            merged_arr[i] = arrA[countA]
            countA = countA + 1
            
        elif(countA >= len(arrA)):
            merged_arr[i] = arrB[countB]
            countB = countB + 1
            
        elif(arrA[countA] <= arrB[countB]):
            merged_arr[i] = arrA[countA]
            countA = countA + 1
        else:
            merged_arr[i] = arrB[countB]
            countB = countB + 1
# [1, 9], [7, 10]
# [1, 7, 9, 10]
            

    # print(merged_arr)
    return merged_arr


# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):

    if(len(arr) > 1):
        midpoint = len(arr)//2
        LHS = arr[:midpoint]
        RHS = arr[midpoint:]
        left = merge_sort(LHS)
        right = merge_sort(RHS)
        return merge(left, right)
        
    print(arr)
    return arr
print(merge_sort([3, 5, 7, 2, 24]))

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

#quicksort: has a pivot point, splits work in smaller chunks and sorts around a pivot point
def partition(arr):
    # pick a pivot
    pivot = arr[0]
    left = []
    right = []

    for i in arr[1:]:
        if i <= pivot:
            left.append(i)
        else:
            right.append(i)
    # we have elements partitioned in the left pivot and right arrays
    return left, pivot, right

def quicksort(arr):
    # base case
    # if the length of the array is less than or equal to one
    if len(arr) <= 1:
        return arr
    # otherwise, we need to call our partition function to break the input up
    left, pivot, right = partition(arr)
    return quicksort(left) + [pivot] + quicksort(right)

# merge sort:
# break the array in half
# keep breaking it in half
# until the length of each array is one
# swap elements 2 at a time
# append swapped elements into their own arrays
# take new pairs of arrays
# compare each pair, take the first elements and compare them
# iterate over the rest and compare them
# append to new array
# repeat, appending as necessary
# 