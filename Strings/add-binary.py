def addBinary(a, b):
    """
    :type a: str
    :type b: str
    :rtype: str
    """
    i = len(a)-1
    j = len(b)-1
    out = ''
    carry = 0
    while i >= 0 or j >= 0:
        v1 = 0 if i < 0 else int(a[i])
        v2 = 0 if j < 0 else int(b[j])
        x = v1+v2+carry
        if x == 1:
            carry = 0
            out += '1'
        elif x == 2:
            carry = 1
            out += '0'
        elif x == 3:
            carry = 1
            out += '1'
        elif x == 0:
            carry = 0
            out += '0'
        i-=1
        j-=1

    if carry:
        out += str(carry)
    return out[::-1]

a = "0"
b = "0"
print(addBinary(a,b))