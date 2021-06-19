def solve(A, b): 
    count = 0
    n = len(A)
    totas = 0
    for i in range(len(A)):
        if A[i] == 1:
            count = 1

            # left corner case
            if i-b+1 > 0:
                return -1
            print("i=",i)
            j = n-1
            max_postn = i+b-1
            while j >= max_postn:
                print("j=",j)
                if A[j] == 1:
                    last_min_postn = j-b+1
                    count += 1
                    print(max_postn,last_min_postn)
                    if last_min_postn <= max_postn:
                        return count
                j-=1
A = [ 0, 0, 1, 1, 1, 0, 0, 1]
B = 3
print(solve(A,B))