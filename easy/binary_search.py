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
        

    def search(self, nums: List[int], target: int) -> int:
        low , high = 0, len(nums)-1
        res = self.binary_search(low, high, target, nums)

        return res