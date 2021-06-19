def findPeakElement(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    
    def bs(i,j,A):
        if j <= i:
            if i == j == 0:
                if A[i] > A[i+1]:
                    return i
            if i == j == len(A)-1:
                if A[j-1] < A[j]:
                    return j
            return None 
        else:
            mid = (i+j)//2
            # check if mid is pivot
            if A[mid] > A[mid-1] and A[mid] > A[mid+1]:
                return mid
            else:
                val = bs(i,mid,A)
                if val == None:
                    return bs(mid+1,j,A)
                return val
    
    if len(nums) == 1:
        return 0
    return bs(0,len(nums)-1,nums)

A = [2,1]
print(findPeakElement(A))
