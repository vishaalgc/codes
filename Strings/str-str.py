def strStr(haystack, needle):
    """
    :type haystack: str
    :type needle: str
    :rtype: int
    """
    if not needle and not haystack:
        return 0
    if not needle:
        return 0
    if not haystack:
        return -1
    
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
                j=0
                break
        if j == len(needle):
            return index
        i = index+1
        
    return index

A = "aaa"
B = "aaaa"

print(strStr(A,B))