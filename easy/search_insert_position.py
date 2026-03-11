class Solution:

    def binary_search(self, l, h , n, nums) -> int:
        if(l>h):
            return -1
        
        mid = l + (h-l)//2
        if(n == nums[mid]):
            return mid
        elif ( n < nums[mid]):
            return self.binary_search(l, mid-1, n, nums)
        else:
            return self.binary_search(mid+1, h, n, nums)
        

    def searchInsert(self, nums: List[int], target: int) -> int:
        low , high = 0, len(nums)-1
        res = self.binary_search(low, high, target, nums)

        if(res == (-1)):
            
            if(nums[high] < target):
                return len(nums)
            elif(nums[0] > target):
                return 0
            else:
                for i in range(0, len(nums)-1):
                    if( nums[i]<target and nums[i+1] > target):
                        return i+1

        else:
            return res