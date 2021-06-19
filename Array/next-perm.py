def revList(A,i,j):
    while i <= j:
        swap(A,i,j)
        i+=1
        j-=1
        
def swap(A,i,j):
    temp = A[i]
    A[i] = A[j]
    A[j] = temp
    
# @param A : list of integers
# @return a list of integers
def nextPermutation( A):
    
    # find pivot
    n = len(A)
    i = n-1
    found = False
    while i > 0:
        if A[i-1] < A[i]:
            found = True
            break
        i-=1
        
        
        
    # theres no pivot [n-2] [n-1] swap
    if not found:
        swap(A,n-2,n-1)
        return A
        
        
        
    # i is pivot
    small = A[i]
    small_index = i
    # find in suffix biffer than i-1th element and smallest in suffix
    
    j = i+1
    while j < n:
        if A[j] > A[i-1]:
            if A[j] < small:
                small_index = j
                small = A[j]
        j+=1
    
    # theres no small element on right
    if small_index == i:
        # store i-1 val
        # from pivot to n move all elements to left 1 postn
        vl = A[i-1]
        j = i
        swap(A,i-1,i)
        revList(A,i,n-1)
        return A
        
    
    # swap small index and i-1
    swap(A,small_index,i-1)
    
    # sort i+1 -> n as decreasing
    revList(A,i,n-1)
    
    return A