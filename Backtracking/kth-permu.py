def getPermutation( n, k):
    def bfs(k):
        val = 1
        x = 1
        count = 0
        offset = k
        fact = 1
        while val < k:
            fact*=x
            count+=1
            val = fact
            x+=1
            
        return count

    def convertListToStr(lt):
        if not lt:
            return ''
        st = ''
        for i in lt:
            st+=str(i)
        return st
            
    def fact(n):
        if n == 0:
            return 1
        val = 1
        while n > 0:
            val *= n
            n-=1
        return val
        

    def findBatch(n,k):
        val = 0
        eachBatchCount = fact(n-1)
        print("eachBatchCount",eachBatchCount,"n",n,"k",k)
        index = 0

        # index = k//eachBatchCount
        # offset = k%eachBatchCount
        # return index,offset


        while val < k:
            val += eachBatchCount
            index+=1

        if index == 0:
            return (0,k)

        val-=eachBatchCount
        offset = k-val
        return (index-1,offset)

    def recur(i,n,A,lt,results,k):
        if i == n and len(results) < k:
            results.append(1)
            if len(results) == k:
                results.append(convertListToStr(lt))

        else:
            for j in range(len(A)):
                item = A[j]
                del A[j]
                lt.append(item)
                recur(i+1,n,A,lt,results,k)
                del lt[-1]
                A.insert(j,item)
                
    m = 1
    A = []
    while m <= n:
        A.append(m)
        m+=1
        
    head = ''
    if k == 1:
        return convertListToStr(A)

    offset = k
    lastOffset = k
    while offset != 0:
        lastOffset = offset
        index,offset = findBatch(len(A),offset)
        print(index,offset,n,k)
        if not A:
            return head
        head += str(A[index])
        del A[index]
        print(A)

    # lt = []
    # results = []
    # print(A)
    # recur(0,len(A),A,lt,results,offset)
    # st = head
    # if results:
    #     st+=str(results[-1])
    # return st

print(getPermutation(3,2))