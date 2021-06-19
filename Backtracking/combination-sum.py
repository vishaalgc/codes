def combinationSum(candidates, target):
    """
    :type candidates: List[int]
    :type target: int
    :rtype: List[List[int]]
    """
    
    def recur(sm,target,A,lt,results):
        if sm == target:
            xt = list(lt)
            xt.sort()
            if xt not in results:
                results.append(xt)
        else:
            for j in range(0,len(A)):
                item = A[j]
                sm+=item
                lt.append(item)
                if sm <= target:
                    recur(sm,target,A,lt,results)
                del lt[-1]
                sm-=item
    
    lt = []
    results = []
    recur(0,target,candidates,lt,results)
    return results

A = [2,3,6,7]
B = 7
print(combinationSum(A,B))