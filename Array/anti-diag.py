def adder(A,i,j,lt):
    if i == j:
        lt.append([A[i][j]])
    else:
        m = i
        n = j
        xt = []
        while m <= j and n >= m:
            xt.append(A[m][n])
            m+=1
            n-=1
        xt.reverse()
        lt.append(xt)
    
    
def diagonal( A):
    lt = []
    n = len(A)-1 
    i = 0
    j = 0
    
    while j <= n:
        adder(A,i,j,lt)
        j += 1
    
    j = n
    while i <= n:
        adder(A,i,j,lt)
        i += 1
        
    return lt