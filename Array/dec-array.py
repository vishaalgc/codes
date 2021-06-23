def checkPossibility(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    one = list(nums)
    two = list(nums)
    
    found = False
    for i in range(len(nums)-1):
        if nums[i]  > nums[i+1]:
            if found:
                return False
            one[i] = one[i+1]
            two[i+1] = two[i]
            found = True
    
    sortOne = True
    for i in range(len(one)-1):
        if one[i] > one[i+1]:
            sortOne = False
            break

    sortTwo = True
    for i in range(len(two)-1):
        if two[i] > two[i+1]:
            sortTwo = False
            break
    
    print(one)
    print(two)
    return sortOne or sortTwo

A = [4,2,3]
A = [5,7,1,8]
# A = [4,2,1]
print(checkPossibility(A))