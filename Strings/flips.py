def minFlipsMonoIncr( s):
    """
    :type s: str
    :rtype: int
    """
    
    prefix = [0]
    for i in range(len(s)):
        prefix.append(prefix[i]+ (0 if s[i] == '0' else 1))
    
    suffix = [0]
    j = 0
    for i in range(len(s)-1,-1,-1):
        suffix.append(suffix[j] + (1 if s[i] == '0' else 0))
        j+=1
    
    suffix = suffix[::-1]
    
    flips = len(s)-1
    for i in range(len(prefix)):
        leftOnes = prefix[i]
        rightZeroes = suffix[i]
        flips = min(flips, leftOnes + rightZeroes)
    
    return flips

s = "00110"
# s = "010110"
# s = "00011000"
# s = "0101100011" 

print(minFlipsMonoIncr(s))