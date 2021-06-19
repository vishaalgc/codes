def combine(n, k):
    """
    :type n: int
    :type k: int
    :rtype: List[List[int]]
    """
    def recur(A,k,lt,results):
        if k == len(lt):
            xt = list(lt)
            results.append(xt)
        else:
            for j in range(len(A)):
                item = A[j]
                lt.append(item)
                mt = A[j+1:]
                recur(mt,k,lt,results)
                del lt[-1]
    
    
    A = []
    for i in range(1,n+1):
        A.append(i)      
    lt = []
    results = []
    recur(A,k,lt,results)
    return results

print(combine(4,2))