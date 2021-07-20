class Solution:
    def maxAreaIn1D(self,arr):
        st = []
        maxArea = 0
        i = 0
        while i < len(arr):
            if not st or arr[i] >= arr[st[-1]]:
                st.append(i)
                i+=1
            else:
                poppedIndex = st[-1]
                st.pop()
                if st:
                    maxArea = max(maxArea,(i-st[-1]-1)*arr[poppedIndex])
                else:
                    maxArea = max(maxArea,(i)*arr[poppedIndex])                  
    
        while st:
            poppedIndex = st[-1]
            st.pop()
            if st:
                maxArea = max(maxArea,(i-st[-1]-1)*arr[poppedIndex])
            else:
                maxArea = max(maxArea,(i)*arr[poppedIndex])    
                
        return maxArea
    
    def largestRectangleArea(self, heights) -> int:
        return self.maxAreaIn1D(heights)
        
s = Solution()
heights = [2,1,5,6,2,3]
print(s.largestRectangleArea(heights))