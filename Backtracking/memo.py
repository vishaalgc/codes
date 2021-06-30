#2. https://leetcode.com/problems/best-time-to-buy-and-sell-stock/


class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        def recur(startIndex,prices,memo):
            if startIndex in memo:
                return memo[startIndex]

            if startIndex >= len(prices):
                return 0
            startPrice = prices[startIndex]
            sm = 0
            bestVal = 0
            for i in range(startIndex+1,len(prices)):
                if prices[i] > startPrice:
                    item = (prices[i]-startPrice)
                    sm+=item
                    for j in range(i+1,len(prices)):
                        val = recur(j,prices,memo)
                        sm+=val
                        bestVal = max(bestVal,sm)
                        sm-=val
                    bestVal = max(bestVal,sm)
                    sm-=item
            memo[startIndex] = bestVal
            return bestVal
            

        memo = {}
        maxVal = 0
        for i in range(len(prices)):
            val  = recur(i,prices,memo)
            maxVal = max(maxVal,val)
        return maxVal

A = [2,6,8,7,8,7,9,4,1,2,4,5,8]
# A = [7,1,5,3,6,4]
# A = [1,2,3,4,5]
# A = [7,6,4,3,1]
# A = [3,2,6,5,0,3]
s = Solution()
print(s.maxProfit(A))
                    
        