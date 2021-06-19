def adder(A,i,j,n,start):
    if n < i:
        return A
    
    if i == j == n:
        A[i][j] = start
        return A
    i_bkp = i
    j_bkp = j
    while j <= n:
        A[i][j] = start
        start+=1
        j+=1
    j-=1
    
    i = i_bkp
    i += 1
    while i <= n:
        A[i][j] = start
        start+=1
        i += 1
    
    j = n-1
    i = n
    
    while j >= j_bkp:
        
        A[i][j] = start
        start+=1
        j -= 1
    

    i = n-1
    j = j_bkp
    
    while i > i_bkp:
        A[i][j] = start
        start+=1
        i-=1
    return adder(A,i_bkp+1,j_bkp+1,n-,start)
    
# @param A : integer
# @return a list of list of integers
def generateMatrix(A):
    v = []
    for i in range(A):
        x = []
        for j in range(A):
            x.append(-1)
        v.append(x)
    return adder(v,0,0,A-1,1)


print(generateMatrix(3))