#Given a sorted and rotated array, find if there is a pair with a given sum

inps = [[11, 15, 6, 8, 9, 10],[11, 15, 26, 38, 9, 10]]


def findPairs(A,pairSum):
    i = 0
    j = len(A)-1
    pairs = []
    while i <= j:
        if A[i] + A[j] == pairSum:
            pairs.append((A[i],A[j]))
            break
        elif A[i] + A[j] > pairSum:
            j-=1
        else:
            i+=1
    return pairs


def rotateArray(A,d):
    lt = []
    n = len(A)
    for i in range(n):
        lt.append(A[(i+d)%n])
    return lt

def findPivotIndex(A,i,j):
    if i > j:
        return -j

    if j-i == 1 and A[i] > A[j]:
        return j

    mid = int((i+j)/2)

    if A[i] <= A[mid]:
        return findPivotIndex(A,mid,j)
    else:
        return findPivotIndex(A,i,mid)



def search(A,i,j,key):
    for i in A:
        if key-i in A and A.index(i) != A.index(key-i):
            return (i,key-i)
    return -1


for inp in inps:
    timesToRotate = findPivotIndex(inp,0,len(inp)-1)
    # print(timesToRotate)
    inp = rotateArray(inp,timesToRotate)
    print(inp)
    print(findPairs(inp,16))