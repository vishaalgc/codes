def spiral(A,i,j,b,d,out):
    if b < 0 or d < 0:
        return out
    elif d == 0:
        while b >= 0:
            out.append(A[i][j])
            j+=1
            b-=1
        return out
    elif b == 0:
        while d >= 0:
            out.append(A[i][j])
            i+=1
            d-=1
        return out
    else:
        x = b
        y = d
        while x > 0:
            out.append(A[i][j])
            j+=1
            x-=1
        while y > 0:
            out.append(A[i][j])
            i+=1
            y-=1
        x = b
        y = d
        while x > 0:
            out.append(A[i][j])
            j-=1
            x-=1
        while y > 0:
            out.append(A[i][j])
            i-=1
            y-=1
        return spiral(A,i+1,j+1,b-2,d-2,out)
        
def spiralOrder(A):
        lt = spiral(A,0,0,len(A[0])-1,len(A)-1,[])
        if not lt:
            return A[0][0]
        return lt



A = [
  [1],
  [2],
  [3]
]
print(spiralOrder(A))