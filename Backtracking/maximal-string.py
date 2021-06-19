def solve(self, A, B):
    out = A
    
    def swap(i,j,A):
        temp = A[i]
        A[i] = A[j]
        A[j] = temp

    def recur(A,B):
        if B <= 0:
            return out
        else:
            for i in range(len(A)):
                for j in range(i+1,len(A)):
                    if A[j] > A[i]:
                        swap(i,j,A)
                        if out < ''.join(A):
                            out = ''.join(A)
                        recur(A,B-1)
                        swap(i,j,A)

    recur(list(A),B)
    return out