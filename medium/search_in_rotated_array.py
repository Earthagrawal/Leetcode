class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        h = len(nums) - 1
        ans = -1
        while (l<=h):
            m = (l + (h - l)//2)
            if nums[m] == target:
                return m

            if nums[l] <= nums[m]:
                if (target <= nums[m]) and (target >= nums[l]):        
                    h = m - 1
                else:
                    l = m + 1

            else:
                if (target >= nums[m]) and (target <= nums[h]):
                    l = m + 1
                else:
                    h = m - 1

        return ans
