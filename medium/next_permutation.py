class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        flag=-1
        if(n>1):

            for i in range(n-2,-1,-1):
                if(nums[i]<nums[i+1]):
                    flag=i
                    break
            
            if(flag == -1):
                x = sorted(nums)
                nums[:] = x
            else:
                for i in range(n-1,flag,-1):
                    if(nums[i] > nums[flag]):
                        nums[i], nums[flag] = nums[flag], nums[i]
                        nums[flag+1:] = sorted(nums[flag+1:])
                        break
        