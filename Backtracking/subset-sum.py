# Subset of sum problem


def isValid(sm,B):
    if sm  <= B:
        return True
    return False


def recur(sm,B,A,lt,results):
    if sm == B:
        x = list(lt)
        x.sort()
        if x not in results:
            results.append(x)
    else:
        for j in range(len(A)):
            item = A[j]
            sm += item
            lt.append(item)
            del A[j]
            if isValid(sm,B):
                recur(sm,B,A,lt,results)
            del lt[-1]
            sm-=item
            A.insert(j,item)


A = [5, 6, 12 , 54, 2 , 20 , 15]
n = len(A)
B = 25
lt = []
results = []

recur(0,B,A,lt,results)
for i in results:
    print(i)
