def maxLength(arr):
    """
    :type arr: List[str]
    :rtype: int
    """
    
    def isUniq(st):
        mp = {}
        for i in st:
            if i in mp:
                return False
            else:
                mp[i]=True
        return True
    
    lt = []
    remove = []
    prevIndexes = []
    for i in range(len(arr)):
        if isUniq(arr[i]):
            lt.append(len(arr[i]))
            prevIndexes.append(-1)
        else:
            remove.append(i)
        
    print(remove)
        
    for i in remove:
        del arr[i]

    if not lt:
        return 0

    for i in range(len(arr)):
        for j in range(0,i+1):
            val = arr[i]+arr[j]
            if isUniq(val):
                # check if j has prevIndexes
                k = j
                while prevIndexes[k] != -1:
                    k = prevIndexes[k]
                    lastVal = val
                    val += arr[k]
                    if not isUniq(val):
                        val = lastVal
                        break
                
                if len(val) > lt[i]:
                    lt[i] = len(val)
                    prevIndexes[i] = j
                

    return max(lt)


A = ["a", "abc", "d", "de", "def"]
A = ["un","iq","ue"]
A = ["abcdefghijklmnopqrstuvwxyz"]
A = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p"]
A = ["cha","r","act","ers"]
A = ["yy","bkhwmpbiisbldzknpm"]
print(maxLength(A))