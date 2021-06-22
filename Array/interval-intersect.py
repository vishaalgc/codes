def intervalIntersection( firstList, secondList):
    """
    :type firstList: List[List[int]]
    :type secondList: List[List[int]]
    :rtype: List[List[int]]
    """
    def intersect(a,b):
        out = []
        # we check if there is scope for intersection
        if a[1] < b[0] or a[0] > b[1]:
            return out
        return [max(a[0],b[0]),min(a[1],b[1])]
    
    if not secondList or not firstList:
        return []
    

    out = []
    i,j = 0,0
    n1,n2 = len(firstList),len(secondList)
    
    while i < n1 and j < n2:
        v1 = firstList[i]
        v2 = secondList[j]
        val = intersect(v1,v2)
        if val:
            out.append(val)
        if v1[1] >= v2[1]:
            j+=1
        else:
            i+=1
    return out

firstList = [[0,2],[5,10],[13,23],[24,25]]
secondList = [[1,5],[8,12],[15,24],[25,26]]

print(intervalIntersection(firstList,secondList))