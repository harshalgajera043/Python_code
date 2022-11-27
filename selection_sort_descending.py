def rselSort(A):
    """assumes that L is a list of element that can be 
    compared using >.
    sorts L in descending order"""

    for i in range(len(A)):
        max_idx = i
        for j in range(i+1, len(A)):
            if A[j] > A[max_idx]:
                 max_idx = j

        A[i], A[max_idx] = A[max_idx], A[i]
    return A

L = [35, 76, 3, 65, 99, 69, 32] 

print('sorted list is: ',rselSort(L))
                
