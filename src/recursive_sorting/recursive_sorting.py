# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = []
    # TO-DO
    if len(arrA) == 0:
        return arrB
    if len(arrB) == 0:
        return arrA

    a_index = 0
    b_index = 0

    while len(merged_arr) < elements:
        if arrA[a_index] <= arrB[b_index]:
            merged_arr.append(arrA[a_index])
            a_index += 1
        else:
            merged_arr.append(arrB[b_index])
            b_index += 1

        if a_index == len(arrA):
            merged_arr += arrB[b_index:]
            break
        elif b_index == len(arrB):
            merged_arr += arrA[a_index:]
            break

    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    # TO-DO
    if len(arr) <= 1:
        return arr
    else:
        middle = len(arr) // 2
        left, right = arr[:middle], arr[middle:]
        return merge(merge_sort(left), merge_sort(right))


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr


def merge_sort_in_place(arr, l, r):
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):

    return arr
