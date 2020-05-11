# selection sort
# O(n^2)

# Import numpy only to create random lists as inputs
import numpy as np 

def selection_sort(seq):
    print("Unsorted array", seq)
    for i in range(len(seq)):
        for j in range(i+1, len(seq)):
            if seq[j] < seq[i]:
                seq[i], seq[j] = seq[j], seq[i]
    return seq


print("Sorted array", selection_sort(np.random.randint(20, size=20)))