def f(A,i,j):
    if i == j:
        return
    return abs(A[i] - A[j]) + abs(i - j)
        
def maxArr(A):
    n = len(A)
    i = 1
    max_val = 0
    while i <= n:
        j = i+1
        while j <= n:
            max_val = max(f(A,i-1,j-1),max_val)
            j+=1
        i+=1
    return max_val

A=[1, 3, -1]
print(maxArr(A))