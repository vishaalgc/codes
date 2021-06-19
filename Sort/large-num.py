
#TC - O(nlogn)
#SC - O(n)

import math
inps = [[1,16,12,0,98,25,2,4],[50, 9, 18, 61, 32],[23, 9, 50, 18, 61, 32],[8,89],[0,0,0]]

#swaps elements in the array
def swap(arr,i,j):
    x = arr[i]
    arr[i] = arr[j]
    arr[j] = x

def comp(A,i,j):
    m = int(str(A[i])+str(A[j]))
    n = int(str(A[j])+str(A[i]))
    if m < n:
        return True
    return False

def merge(arr,i,m,k,j):
    #Iteration stopper condition
    if(j-i == 1):
        if comp(arr,i,j):
            swap(arr,i,j)
            print(arr)
    else:       
        x= []
        p1 = i
        p2 = k
        #Compare 2 arrays and create new one
        while p1 <= m and p2 <= j:
            if not comp(arr,p1,p2):
                x.append(arr[p1])
                p1+=1
            else:
                x.append(arr[p2])
                p2+=1

        #leftover elements from any of the arrays above to be attached at end of the list
        if p1 <= m:
            while p1 <= m:
                x.append(arr[p1])
                p1+=1
        elif p2 <= j:
            while p2 <= j:
                x.append(arr[p2])
                p2+=1

        #sync this new list with actual arr
        l = 0
        while i <= j:
            arr[i] = x[l]
            i+=1
            l+=1
    
    

def mergeSort(arr,i,j):
    if(i != j):
        mid = math.floor((i+j)/2)
        mergeSort(arr,i,mid)
        mergeSort(arr,mid+1,j)
        merge(arr,i,mid,mid+1,j)


for inp in inps:
    mergeSort(inp,0,len(inp)-1)
    print(inp)
    
    