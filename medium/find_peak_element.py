class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l,h = 0, len(nums)-1
        n=len(nums)

        while(l<=h):
            m = (l+h)>>1

            if((m==0  or nums[m-1]<nums[m]) and (m==(n-1) or nums[m]>nums[m+1] )):
                return m
            elif( m!=0 and nums[m-1]> nums[m]):
                h=m-1
            elif(m!=(n-1) and nums[m+1]>nums[m]):
                l=m+1
        