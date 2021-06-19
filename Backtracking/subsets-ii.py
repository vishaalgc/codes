
def recur(i,n,A,lt,results):
    if i > n:
        return
    else:
        x = list(lt)
        if x not in results:
            results.append(x)
        for j in range(len(A)):
            item = A[j]
            lt.append(item)
            xt = A[j+1:len(A)]
            recur(i+1,n,xt,lt,results)
            del lt[-1]
            

A = [1,2,2,2,4]
A.sort()
n = len(A)
lt = []
results = []
recur(0,n,A,lt,results)


# results.sort()
# for i in results:
#     print(i)

print(results)

# [] [1 ] [1 2 ] [1 2 2 ] [1 2 2 2 ] [1 2 2 2 4 ] [1 2 2 4 ] [1 2 4 ] [1 4 ] [2 ] [2 2 ] [2 2 2 ] [2 2 2 4 ] [2 2 4 ] [2 4 ] [4 ]