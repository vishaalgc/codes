def nextGreaterElements(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    
    def greaterElemsFromLeft(A):
        val = A[0]
        out= [-2**31]
        for i in range(1,len(A)):
            if A[i] < val:
                out.append(val)
            if A[i] >= val:
                out.append(-2**31)
                val = A[i]

        return out

    def leftGreater(A):
        lt = []
        rt = []

        for i in range(len(A)):
            while lt and A[i] >= lt[-1]:
                lt.pop()
            if lt:
                rt.append(lt[-1])
            else:
                rt.append(-2**31)
            lt.append(A[i])
        return rt

    def rightGreater(A):
        lt = []
        rt = []

        for i in range(len(A)-1,-1,-1):
            while lt and A[i] >= lt[-1]:
                lt.pop()
            if lt:
                rt.append(lt[-1])
            else:
                rt.append(-2**31)
            lt.append(A[i])
        return rt[::-1]

    left = leftGreater(nums)
    right = rightGreater(nums)
    leftMost = greaterElemsFromLeft(nums)
    # leftMost = leftGreater(nums[::-1])[::-1]

    print(nums)
    # print(left)
    # print(right)
    print(leftMost)

    out = []
    for i in range(len(left)):
        v1 = right[i]
        if v1 == -2**31:
            v1 = leftMost[i]
        v2 = left[i]
        if v2 == -2**31:
            v2 = right[i]
        val = max(v1,v2)
        if val == -2**31:
            val = -1
        out.append(val)
    return out

A = [1,2,3,2,1]

print(nextGreaterElements(A))