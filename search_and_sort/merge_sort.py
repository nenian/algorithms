# merge sort 
# time complexity: O(nlogn)

import random 
def combine(left, right):
    i, j = 0, 0
    combined = []
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            combined.append(left[i])
            i += 1
        else:
            combined.append(right[j])
            j += 1   

    if i == len(left):
        combined.extend(right[j:])
    elif j == len(right):
        combined.extend(left[i:])
    return combined


def merge_sort(mylist):
    list_length = len(mylist)
    if list_length < 2:
        return mylist[:]
    else:
        mid = list_length//2
        left = merge_sort(mylist[:mid])
        right = merge_sort(mylist[mid:])
        return combine(left, right)

merge_sort(random.sample(range(-100, 500), 200))


