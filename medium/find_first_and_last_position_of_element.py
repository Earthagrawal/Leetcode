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

    def lower_binary_search(self, l,h, n,nums):
        if(l>h):
            return len(nums)-1

        mid = l + (h-l)//2
        if(nums[mid] < n):
            return self.lower_binary_search(mid+1, h, n, nums)
        
        elif( nums[mid] == n ):
            i = mid
            j = self.lower_binary_search(l, mid-1, n, nums)
            return min(i,j)

        else:
            return self.lower_binary_search(l, mid-1, n, nums)

    def higher_binary_search(self, l,h, n,nums):
        if(l>h):
            return 0

        mid = l + (h-l)//2
    
        if(n < nums[mid]):
            return self.higher_binary_search(l, mid-1, n, nums)

        elif(n > nums[mid]):
            return self.higher_binary_search(mid+1, h, n, nums)

        else:
            i = mid
            j = self.higher_binary_search( mid+1, h, n, nums)
            return max(i,j)
            

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        ans = [-1,-1]

        l = 0
        h = len(nums)-1

        res = self.binary_search(l,h,target, nums)
        if(res == -1):
            return ans
        else:
            lower = self.lower_binary_search(l,h,target, nums)
            higher = self.higher_binary_search(l,h,target, nums)

            return [lower, higher]


            