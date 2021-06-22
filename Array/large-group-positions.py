def largeGroupPositions(s):
    """
    :type s: str
    :rtype: List[List[int]]
    """
    count = 0
    lastI = -1
    maxSoFar = 3
    out = []
    for i in range(len(s)):
        if count == 0:
            count+=1
            lastI = i
        else:
            if s[i] != s[i-1]:
                if  count >= maxSoFar:
                    out.append([lastI,i-1])
                count = 1
                lastI = i
            else:
                count+=1

    if count >= maxSoFar:
        out.append([lastI,len(s)-1])
    out.sort()
    return out

s = "aaa"
print(largeGroupPositions(s))
