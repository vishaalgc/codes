def swap(A,i,f,j,k):
    print(i,f)
    temp = A[i][f]
    A[i][f] = A[k][j]
    A[k][j] = temp
    
# @param A : list of list of integers
# @return the same list modified
def rotate(A):
    m = len(A)-1
    i = m
    j = m
    f = 0
    
    while f < m:
        while i != 0 and j != 0 and i >= f and j >= f:
            swap(A,i,f,j,f)
            i -= 1
            j -= 1
        f+=1

        i = m
        j = m
        
    for i in A:
        i = i.reverse()
    
    return A

A = [
  [31, 32, 228, 333],
  [79, 197, 241, 246],
  [77, 84, 126, 337],
  [110, 291, 356, 371],
]

print(rotate(A))