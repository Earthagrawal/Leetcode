class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
         
        left = 1  
        right = max(piles)
        size = int(len(piles))  
        ans = 0 

        while(left<=right):
            mid = left + ( (-left + right)>>1)

            res=0
            for i in piles:
                res+= math.ceil(i/mid)
            
        
            
            if(res > h):
                left = mid+1
            
            elif(res <= h):
                ans=mid
                right = mid-1

            print("ans value", ans)
            
        return ans
            
       