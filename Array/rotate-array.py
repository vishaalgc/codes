inps = [[1,16,12,0,98,25,2,4],[50, 9, 18, 61, 32],[23, 9, 50, 18, 61, 32]]
B = 2


# Here i+b is used because our first element will be in (i+b)th position after rotation. 
# As b increases and i+b crossed n we use % to get to the start of the array and populate rest of the elements
# LEFT TO RIGHT Rotation 1 2 3 4 5 [2] => 3 4 5 1 2
# We use i+n-b for RIGHT ROTATION 1 2 3 4 5 [2] => 4 5 1 2 3
def rotArray(arr,b,n):
    lt = ''
    for i in range(n):
        lt += arr[(i+b)%n] + ' '
    return lt[:-1]

for inp in inps: 
    rotArray(inp,2,len(inp))
    print(inp)
    