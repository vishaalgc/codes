vl = 0

def merge(arr,i,m,n,j,ctr):
    if j-i == 1:
        if arr[i] > arr[j]:
            print(arr[i],arr[j])
            tmp = arr[i]
            arr[i] = arr[j]
            arr[j] = tmp
            ctr+=1
    else:
        p1 = i
        p2 = n
        x = []
        while p1 <= m and p2 <= j:
            if arr[p1] <= arr[p2]:
                x.append(arr[p1])
                p1+=1
            else:
                ctr+=1
                print("-->",arr[p1],arr[p2])
                x.append(p2)
                p2+=1
        
        while p1 <= m:
            x.append(p1)
            p1+=1
        while p2 <= j:
            x.append(p2)
            p2+=1
        
        
        l = 0
        while i <= j:
            arr[i] = x[l]
            i+=1
            l+=1
            
    return ctr
        
            
            
    
    
def mergeSort(arr,i,j,ctr):
    global vl
    if i != j:
        mid = int((i+j)/2)
        mergeSort(arr,i,mid,ctr)
        mergeSort(arr,mid+1,j,ctr)
        ctr = merge(arr,i,mid,mid+1,j,ctr)
        vl += ctr

def hotel(arrive, depart, K):
    mp = {}
    if K <=0 :
        return 0
    A = []
    for i,j in zip(arrive,depart):
        A.append(i)
        A.append(j)
    ctr = 0
    mergeSort(A,0,len(A)-1,ctr)
    
    print(vl,K)
    if vl >= K:
        return 0
    else:
        return 1

A = [ 36, 45, 41, 7, 3, 44, 40, 46, 3, 16, 24, 3, 8, 33 ]
B = [ 71, 73, 85, 8, 11, 62, 64, 76, 25, 65, 25, 30, 36, 81 ]
C = 14
print(hotel(A,B,C))