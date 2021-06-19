def checker(A,i,n):
    print("i=",i)
    k = i
    left = -1
    right = -1
    left_big = A[i]
    right_small = A[i]
    val = A[i]
    k-=1
    while k > 0:
        if val < A[k]:
            if(A[k] > left_big):
                left_big = A[k]
                left = k
        k-=1
    
    k = i+1
    while k < n:
        if val > A[k]:
            if A[k] < right_small:
                right_small = A[k]
                right = k
        k+=1
    
    print(left_big,right_small,left,right)
    if left != -1 and right != -1:
        return 0
    elif left != -1:
        return checker(A,left,n)
    # elif right != -1:
    #     return checker(A,right,n)
    else:
        return A[i]
        
        
        
        
# @param A : list of integers
# @return an integer
def perfectPeak( A):
    i = int(len(A)/2)
    return checker(A,i,len(A)-1)

A = [ 18757, 13932, 7377, 19955, 24085, 4967, 11841, 19630, 16945, 12624, 24627, 32440, 26309 ]

print(perfectPeak(A))