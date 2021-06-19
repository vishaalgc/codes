#Search an element in a sorted and rotated array
import math

inps = [[5, 6, 7, 8, 9, 10, 1, 2, 3],[30, 40, 50, 10, 20]]


def search(A,i,j,key):
    if i > j:
        return -1
    mid = math.floor((i+j)/2)
    if  A[mid] == key:
        return mid
    
    if A[i] <= A[mid]:
        if A[i] <= key and A[mid] >= key:
            return search(A,i,mid-1,key)
        return search(A,mid+1,j,key)
    
    else:
        if A[mid] <= key and A[j] >= key:
            return search(A,mid+1,j,key)
        return search(A,i,mid-1,key)


for inp in inps:
    print(search(inp,0,len(inp)-1,3))