class Solution:
    def aggressiveCows(self, nums, k):
        nums.sort()

        def check(n):
            m=1
            last = nums[0]
            for i in nums:
                if( i-last >= n ):
                    m+=1
                    last = i
            return m

        left = 1
        right = max(nums) - min(nums)
        ans=left
        while(left <= right):

            mid = (left+ right)//2

            res = check(mid)
            if( res >= k):
                ans = mid
                left = mid+1
            else:
                right = mid-1

        return ans

