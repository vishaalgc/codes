def combinationSum2(candidates, target):
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
                del A[j]
                if sm <= target:
                    recur(sm,target,A,lt,results)
                del lt[-1]
                sm-=item
                A.insert(j,item)

    lt = []
    results = []
    sm = 0
    for i in candidates:
        sm+=i
    if sm < target:
        return []
    recur(0,target,candidates,lt,results)
    results.sort()
    return results

A = [3,1,3,5,1,5,2,3,2,5,4]
B = 1
sm = 0
for i in A:
    sm+=i
print(sm)
print(combinationSum2(A,B))