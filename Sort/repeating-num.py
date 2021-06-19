def repNum(A):
    slow = A[0]; 
    fast = A[A[0]]; 
        
    while slow!=fast:
        slow = A[slow]; 
        fast = A[A[fast]]; 
        
    slow = 0; 
    while slow!=fast:
        slow = A[slow]; 
        fast = A[fast]; 
    
     
    return slow
    

A = [3,4,1,4,2]
print(repNum(A))