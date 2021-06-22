def asteroidCollision(asteroids):
    """
    :type asteroids: List[int]
    :rtype: List[int]
    """
    
    def opposite(p1,p2):
        if p1 > 0 and p2 < 0:
            return True
        return False
    
    def merge(p1,p2):
        v1,v2 = abs(p1),abs(p2)
        if v1 == v2:
            return 0
        if v1 > v2:
            return p1
        return p2
    
    st = []
    for i in asteroids:
        if not st:
            st.append(i)
        else:
            j = i
            while st and opposite(st[-1],j):
                j = merge(j,st[-1])
                st.pop()
                if j == 0:
                    break 
            if j != 0:
                st.append(j)
    return st

A = [5,10,-5]
print(asteroidCollision(A))
