A = 'AAACAAAA'


lps = [0]
n = len(A)

i = 1
leng = 0
while i < n:
    if A[i] == A[leng]:
        leng+=1
        lps.append(leng)
        i+=1
    else:
        if leng != 0:
            leng = lps[leng-1]
        else:
            lps.append(0)
            i+=1
    
print(lps)



i = 1
j = 0
n = len(A)
lps = [0]
while i < n:
    if A[i] == A[j]:
        j+=1
        lps.append(j)
        i+=1
    else:
        if j != 0:
            j = lps[j-1]
        else:
            lps.append(0)
            i+=1
