


def coverPoints(A,B):
    prev_x = A[0]
    prev_y = B[0]
    tot = 0
    for cur_x,cur_y in zip(A,B):
        x,y = abs(cur_x-prev_x),abs(cur_y-prev_y)
        if x < y:
            tot+=y
        else:
            tot+=x
        prev_x = cur_x
        prev_y = cur_y

    return tot






A = [0,1,2]
B = [0,1,2]
print(coverPoints(A,B))