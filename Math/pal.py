def isPalindrome(x):
    """
    :type x: int
    :rtype: bool
    """
    
    if x < 0:
        return False
    if x < 10:
        return True
    
    i = 1
    while x > i:
        i*=10
    i//=10
    
    val = 0
    xBkp = x
    while x != 0:
        val += (x%10)*(i)
        x//=10
        i//=10

    if val == xBkp:
        return True
    return False

print(isPalindrome(121))