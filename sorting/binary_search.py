#Binary search
#O(log n)

def binary_search(seq, val, start, end):

    mid = int((end - start)/2) + start

    if val == seq[mid]:
        return mid
    elif val > seq[mid]:
        return binary_search(seq, val, start=mid+1, end=end)
    elif val < seq[mid]:
        return binary_search(seq, val, start=start, end=mid-1)

mylist = [1, 4, 7, 9, 11, 12, 14]
print(binary_search(mylist, 14, 0, len(mylist)))