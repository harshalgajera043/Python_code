def selSort(A):
    """assumes that L is a list of element that can be 
    compared using >.
    sorts L in ascending order"""

    for i in range(len(A)):
        min_idx = i
        for j in range(i+1, len(A)):
            if A[min_idx] > A[j]:
                 min_idx = j

        A[i], A[min_idx] = A[min_idx], A[i]
    return A

L = [35, 76, 3, 65, 99, 69, 32] 

print('sorted list is: ',selSort(L))
                
