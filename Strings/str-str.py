def strStr(haystack, needle):
    """
    :type haystack: str
    :type needle: str
    :rtype: int
    """
    def lpsArr(A):
        lps = [0]
        n = len(A)

        i = 1
        leng = 0
        while i < n:
            if A[i] == A[leng]:
                leng+=1
                lps.append(leng)
                i+=1
            else:
                if leng != 0:
                    leng = lps[leng-1]
                else:
                    lps.append(0)
                    i+=1
        return lps


    if not needle and not haystack:
        return 0
    if not needle:
        return 0
    if not haystack:
        return -1
    
    if len(needle) > len(haystack):
        return -1
    if needle == haystack:
        return 0
    
    lps = lpsArr(needle)
    # print(lps)
    i = 0
    j = 0
    index = -1
    while True:
        while i < len(haystack) and haystack[i] != needle[j]:
            i+=1
        if i == len(haystack):
            return -1
        index = i
        while i < len(haystack) and j < len(needle):
            if haystack[i] == needle[j]:
                i+=1
                j+=1
            else:
                j=lps[j]
                print(j,i)
                break
        if j == len(needle):
            return index
        i = index+1
        
    return index

A = "babba"
B = "bbb"

print(strStr(A,B))