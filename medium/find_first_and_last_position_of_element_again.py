class Solution:
            

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left, right = -1 , -1
        n = len(nums)


        temp = bisect.bisect_left( nums , target )
        if (0<=temp <n ) and (nums[temp] == target):
            left = temp
        
        temp = bisect.bisect_right (nums, target)               
        temp-=1
        if ( (0<=temp < n ) and (nums[temp] == target) ): 
            right = temp

        ans = [left, right]
        
        return ans



            