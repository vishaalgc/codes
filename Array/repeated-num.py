def repeatedNumber( A):
        sm = 0
        n = len(A)
        for i in A:    
            sm += i
        
        mult = 1
        for i in A:
            mult = mult*i
        
        act_mult = 1
        for i in range(1,n+1):
            act_mult *= i

        f = act_mult/mult
        print(f)
        a = (sm - (n(n+1)/2) )/ (1-f)
        b = a+ (n(n+1)/2) - sm
        print([a,b])

A = [3,1, 2, 5, 3]
print(repeatedNumber(A))