
def numSplits( s):
    """
    :type s: str
    :rtype: int
    """
    def validCountDistinct(a,b):
        if a == '' or b == '':
            return False
        return len(set(a)) == len(set(b))
    
    
    
    hashL,hashR = {},{}
    for i in range(len(s)):
        hashR[s[i]]=i


    count = 0      
    for i in range(len(s)):
        if s[i] not in hashL:
            hashL[s[i]]=s[i]

        if s[i] in hashR:
            if i == hashR[s[i]]:
                del hashR[s[i]]
        if len(hashL.keys()) == len(hashR.keys()):
            count+=1
        
    return count

A = 'aacaba'
print(numSplits(A))
            
        
        
