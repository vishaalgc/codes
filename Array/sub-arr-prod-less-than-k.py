def numSubarrayProductLessThanK( nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: int
    """
    lt = []
    prod = 1
    for i in range(len(nums)):
        prod*=nums[i]
        if prod<k:
            if not lt:
                lt.append(i)
            else:
                if lt[-1] != -1:
                    lt.append(lt[-1])
                else:
                    lt.append(i)
        else:
            if not lt:
                lt.append(-1)
                prod = 1
            else:
                j = lt[-1]
                while j <= i and prod >= k:
                    prod/=nums[j]
                    j+=1
                if prod >= k:
                    lt.append(-1)
                    prod = 1
                else:
                    lt.append(j)
    
    count = 0
    for i in range(len(lt)):
        if lt[i] != -1:
            count+=((i-lt[i])+1)
    return count


    # This is bactracking solution below. It works but not efficient
    # def recur(k,prod,A,lt,results):
    #     if prod < k:
    #         if lt:
    #             results.append(list(lt))
    #         if len(A) > 0:
    #             item = A[0]
    #             prod*= item
    #             if prod <= k:
    #                 lt.append(item)
    #                 del A[0]
    #                 recur(k,prod,A,lt,results)
    #                 del lt[-1]
    #                 A.insert(0,item)
    #             prod/=item

    # lt = []
    # results = []
    # for i in range(len(nums)):
    #     recur(k,1,nums[i:],lt,results)
    # return len(results)

nums = [5,2,192]
nums = [10,9,10,4,3,8,3,3,6,2,10,10,9,3]
k = 100
k = 19

print(numSubarrayProductLessThanK(nums,k))