class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        minn, maxx = prices[0], prices[0]
        diff =0
        for i in prices:
            if(i<minn):
                minn,maxx=i,i
                
            if(i>maxx):
                maxx=i
            
            diff = max(diff, maxx-minn)

        return diff
