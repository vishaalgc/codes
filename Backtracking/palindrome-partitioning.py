def recur(A,lt,results):
    if len(A) == 0:
        results.append(list(lt))
    else:
        for i in range(len(A)):
            item = A[0:i+1]
            if item == item[::-1]:
                lt.append(item)
                recur(A[i+1:],lt,results)
                del lt[-1]

s = ''
lt = []
results = []
recur(s,lt,results)
print(results)

