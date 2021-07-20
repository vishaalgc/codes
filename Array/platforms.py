class Solution:    
    #Function to find the minimum number of platforms required at the
    #railway station such that no train waits.
    def minimumPlatform(self,n,arr,dep):
        # code here
        a = []
        for i in range(len(arr)):
            a.append([arr[i],dep[i]])
        
        a.sort(key = lambda x : x[0]) 
        
        ans = 0
        # [(0900,0200),(1000,1200)]
        maxSoFar = 0
        for i in range(n):
            j = i+1
            if j >= n:
                break
            if a[i][1] > a[j][0]:
                a[j][0] = a[i][0]
                a[j][1] = max(a[i][1],a[j][1])
                maxSoFar+=1
            else:
                ans = max(ans,maxSoFar)
                maxSoFar = 0
                
        ans = max(ans,maxSoFar)
        return ans+1

arr = [900, 940, 950, 1100, 1500, 1800]
dep = [910, 1200, 1120, 1130, 1900, 2000]
n = 6
arr = [900, 1100, 1235]
dep = [1000, 1200, 1240]
n = 3
s = Solution()
print(s.minimumPlatform(n,arr,dep))