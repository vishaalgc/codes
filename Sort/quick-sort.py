
#TC - O(nlong)
#SC - O(1)

inps = [[1,16,12,0,98,25,2,4],[50, 9, 18, 61, 32],[23, 9, 50, 18, 61, 32],[5,6,2],[ -4, 7, 5, 3, 5, -4, 2, -1, -9, -8, -3, 0, 9, -7, -4, -10, -4, 2, 6, 1, -2, -3, -1, -8, 0, -8, -7, -3, 5, -1, -8, -8, 8, -1, -3, 3, 6, 1, -8, -1, 3, -9, 9, -6, 7, 8, -6, 5, 0, 3, -4, 1, -10, 6, 3, -8, 0, 6, -9, -5, -5, -6, -3, 6, -5, -4, -1, 3, 7, -6, 5, -8, -5, 4, -3, 4, -6, -7, 0, -3, -2, 6, 8, -2, -6, -7, 1, 4, 9, 2, -10, 6, -2, 9, 2, -4, -4, 4, 9, 5, 0, 4, 8, -3, -9, 7, -8, 7, 2, 2, 6, -9, -10, -4, -9, -5, -1, -6, 9, -10, -1, 1, 7, 7, 1, -9, 5, -1, -3, -3, 6, 7, 3, -4, -5, -4, -7, 9, -6, -2, 1, 2, -1, -7, 9, 0, -2, -2, 5, -10, -1, 6, -7, 8, -5, -4, 1, -9, 5, 9, -2, -6, -2, -9, 0, 3, -10, 4, -6, -6, 4, -3, 6, -7, 1, -3, -5, 9, 6, 2, 1, 7, -2, 5 ]]

#swaps elements in the array
def swap(arr,i,j):
    x = arr[i]
    arr[i] = arr[j]
    arr[j] = x

def quickSort(arr,i,j):
    #define pivot index as starting index of the iteration
    pivotIndex = i
    
    if i>=j:
        return
    
    #consider last element as pivot value
    pivotVal = arr[j]

    k = i
    while k < j:
        #comparing every element with pivot value to make decision on swapping
        if(arr[k] <= pivotVal):
            swap(arr,k,pivotIndex)
            pivotIndex = pivotIndex+1
        k = k+1
        
    #After one iteration swap the pivot index element with last element i.e., actual pivot
    swap(arr,j,pivotIndex)

    #left traversal
    quickSort(arr,i,pivotIndex-1)
    #right traversal
    quickSort(arr,pivotIndex+1,j)


for inp in inps:
    quickSort(inp,0,len(inp)-1)
    print(inp)
    