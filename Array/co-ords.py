'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here


def getDir(old,char):
    if old == (-1,0):
        if char == 'L':
            return (0,-1)
        else:
            return (0,1)
    elif old == (0,-1):
        if char == 'L':
            return (1,0)
        else:
            return (-1,0)
    elif old == (1,0):
        if char == 'L':
            return (0,1)
        else:
            return (0,-1)
    else:
        if char == 'L':
            return (-1,0)
        else:
            return (1,0)

def getFinalPoint(dirStr):
    point = (0,0)
    direction = (0,1)
    oldI = None
    summer = 1
    for i in dirStr:
        if i == 'M':
            point =(point[0]+direction[0],point[1]+direction[1])
        else:
            direction = getDir(direction,i)
    return point
            

def findMinOfXAndY(point):
    x,y = point[0],point[1]
    minCord = min(abs(x),abs(y))
    dist = minCord
    item = None
    pt = point
    vals = (0,1)
    if x < 0 and y < 0:
        item = 3
        vals = (-1,-1)
    elif x < 0 and y > 0:
        item = 4
        vals = (-1,1)
    elif x > 0 and y > 0:
        item = 1
        vals = (1,1)
    else:
        item = 2
        vals = (1,-1)
    st = ''
    pt = (0,0)
    while dist > 0:
        st += str(item)
        pt = (pt[0]+vals[0],pt[1]+vals[1])
        dist-=1
    return st,pt
    
def offset(midPoint,finPoint):
    out = ''
    if finPoint[1] == midPoint[1]:
        # we have to go through x
        diff = finPoint[0]-midPoint[0]
        if diff > 0:
            vl = 6
        else:
            vl = 8
        rots = abs(diff)
        while rots > 0:
            out += str(vl)
            rots-=1
    else:
        # we have to go through y
        diff = finPoint[1]-midPoint[1]
        if diff > 0:
            vl = 5
        else:
            vl = 7
        rots = abs(diff)
        while rots > 0:
            out += str(vl)
            rots-=1

    return out+'0'




tcs = input()

for i in range(int(tcs)):
    leng = input()
    dirStr = input()
    finPoint = getFinalPoint(dirStr)
    st , midPoint = findMinOfXAndY(finPoint)
    # print(finPoint,midPoint)
    st += offset(midPoint,finPoint)
    print(st)

# st = 'LMRMLM'
# solve(st)

