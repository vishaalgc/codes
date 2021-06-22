def areSentencesSimilar(s1, s2):
    """
    :type sentence1: str
    :type sentence2: str
    :rtype: bool
    """
    
    s1 = s1.split(" ")
    s2 = s2.split(" ")
    l1,l2 = 0,0
    r1,r2 = len(s1)-1,len(s2)-1
    
    while l1 <= r1 and l2 <= r2 and s1[l1] == s2[l2]:
        l1+=1
        l2+=1
    
    while r1 >= 0 and r2 >= 0 and s1[r1] == s2[r2]:
        r1-=1
        r2-=1
        
    return l1 > r1 or l2 > r2
    

A = "My name is Haley"
B = "My Haley"

A = "A A AAa"
B = "A AAa"

A = "xD iP tqchblXgqvNVdi"
B = "FmtdCzv Gp YZf UYJ xD iP tqchblXgqvNVdi"

A = "of"
B = "A lot of words"

A = "a"
B = "a a"

A = "Eating right now"
B = "Eating"

print(areSentencesSimilar(A,B))
