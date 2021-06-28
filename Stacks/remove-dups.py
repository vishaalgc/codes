def removeDuplicates( s):
    """
    :type s: str
    :rtype: str
    """
    st = []
    lastSeen = None
    for i in range(len(s)):
        if s[i] == lastSeen:
            continue
        lastSeen = None
        if st and s[i] == st[-1]:
            lastSeen = s[i]
            st.pop()
        else:
            st.append(s[i])
    
    
    return ''.join(st)

A = 'abbaca'
print(removeDuplicates(A))