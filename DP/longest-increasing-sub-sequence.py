def lengthOfLIS(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    
    lt = []
    for i in nums:
        lt.append(1)


    for i in range(len(nums)):
        for j in range(0,i+1):
            if A[i] > A[j]:
                lt[i] = max(lt[i],lt[j]+1)
    return max(lt)




A = [10,9,2,5,3,7,101,18]
A = [0,1,0,3,2,3]
print(lengthOfLIS(A))