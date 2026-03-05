class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        n = len(nums)
        maxc=0
        visited  = [0 for i in range(0,n)]
        
        for i in range(0,n):
            j=1
            curr=1
            if ((nums[i]-1) not in s):
                while(nums[i]+j in s):
                    s.remove(nums[i]+j)
                    j+=1
                    curr+=1
                    
            maxc = max(curr,maxc)
        
        return maxc
