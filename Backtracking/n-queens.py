# import Math
# N Queens problem


def isValid(colPlacements):
    if not colPlacements or len(colPlacements) == 1:
        return True
    
    # get the last latest item added
    lastRow = len(colPlacements)-1

    # we check if this is rightly placed
    for i in range(0,len(colPlacements)-1):
        diff = abs(colPlacements[lastRow]-colPlacements[i])
        
        if diff == 0 or diff == lastRow-i:
            return False

    return True




def solveRecursion(start,n,colPlacements,result):

    # GOAL
    if start == n:
        result.append(list(colPlacements))
    else:
        for j in range(0,n):
            # CHOOSE =>  we add a col into rows index here into colPlacements
            colPlacements.append(j)

            # Now we check if our addition was correct
            # CONSTRAINT 
            if isValid(colPlacements):
                solveRecursion(start+1,n,colPlacements,result)

            # Un choose
            del colPlacements[-1]



# we maintain colPlacements list
# each index in this array defined row number 
# each value at that index defines chosen column number for that row for a queen
colPlacements = []

# result object
result = []

# n
n = 4

# call to main function
solveRecursion(0,n,colPlacements,result)

out = []

# result print
print(result)

# for pretty priting
for p in result:
    xt = []
    for i in range(n):
        st = ''
        for j in range(n):
            if p[i] == j:
                st += 'Q'
            else:
                st += '.'
        xt.append(st)
    out.append(xt)

print(out)







