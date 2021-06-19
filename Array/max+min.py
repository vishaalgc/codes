
import math
inps = [[1,16,12,0,98,25,2,4],[50, 9, 18, 61, 32],[23, 9, 50, 18, 61, 32],[ -2, 1, -4, 5, 3 ]]

min = 0
max = 0

def comp(arr,i,j):
    mx = arr[i]
    mn = arr[i]

    if i == j:
        mx = arr[i]
        mn = arr[j]
        return mn,mx
    
    elif j-i == 1:
        if arr[i] < arr[j]:
            return arr[i],arr[j]
        else:
            return arr[j],arr[i]

    else:
        mid = int((i+j)/2)
        mn_l,mx_l = comp(arr,i,mid)
        mn_r,mx_r = comp(arr,mid+1,j)
        print(mn_l,mn_r,mx_l,mx_r)
        return (max(mx_l,mx_r),min(mn_l,mn_r))

         


for inp in inps:
    print(comp(inp,0,len(inp)-1))
    # print(inp)