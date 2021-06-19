
# print all permutations of a string



def isValid(lt,available):
    if not lt or len(lt) == 1:
        return True
    
    lastItem = lt[-1]
    if lastItem in available:
        return True
    return False


def permuRec(i,n,A,lt,results):

    # GOAL
    if i == n:
        results.add(''.join(lt))
    else:
        for j in range(0,len(A)):
            # CONSTRAINT - Delete current element from A for next iteration
            currentElem = A[j]
            lt.append(currentElem)
            del A[j]
            permuRec(i+1,n,A,lt,results)
            # UNCHOOSE
            del lt[-1]
            A.insert(j,currentElem)
    

results = set()
A = list('abab')
lt = []
n = len(A)

permuRec(0,n,A,lt,results)
print(len(results))
results = list(results)
results.sort()
for i in results:
    print(i)

    


