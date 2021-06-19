
def recur(i,n,A,lt,results):
    if i > n:
        return
    else:
        x = list(lt)
        results.append(x)
        for j in range(len(A)):
            item = A[j]
            lt.append(item)
            xt = A[j+1:len(A)]
            recur(i+1,n,xt,lt,results)
            del lt[-1]
            

A = [15,20,12,19,4]
A.sort()
n = len(A)
lt = []
results = []
recur(0,n,A,lt,results)


results.sort()
for i in results:
    print(i)