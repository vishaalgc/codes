inps = [[1,16,12,0,98,25,2,4],[50, 9, 18, 61, 32],[23, 9, 50, 18, 61, 32]]
B = 2

def rev(arr,i,j):
    arr[i:j] = arr[i:j][::-1]
            
# Reverse individual sections first based on given D then reverse whole array 
# A .. D D+1.. B 
# D .. A B .. D+1
# D+1 .. B A .. D
def leftRotate( arr, d, n):
    rev(arr,0,d)
    rev(arr,d,n)
    rev(arr,0,n)
    return arr

for inp in inps:
    print(leftRotate(inp,B,len(inp)))