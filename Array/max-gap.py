def maximumGap(A):
        x = []
        ctr = 0
        for i in A:
            x.append((i,ctr))
            ctr+=1

        x.sort()
        
        lt = []
        for i in x:
            lt.append(i[1])

        i = 0
        mx = 0
        j = len(lt)-1
        while i <= j:
            m = i+1
            while m <= j:
                if lt[m]-lt[i] > mx:
                    mx = lt[m]-lt[i]
                m+=1
            i+=1
        return mx


print(maximumGap([ 1, 10 ]))