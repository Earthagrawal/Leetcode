class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        
        def check(mid):
            m=1
            sum=0
            for i in nums:
                if(sum+i <= mid):
                    sum+=i
                else:
                    m+=1 
                    sum = i
            return m<=k

        
        left = max(nums)
        right = sum(nums)
        while(left < right):

            mid = (left + right)//2

            if check(mid):
                right = mid
            else:
                left = mid+1

        mid = (left + right)//2
        return mid
