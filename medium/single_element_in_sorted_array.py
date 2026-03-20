class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        l,h=0,len(nums)-1
        while(l<=h):
            m = (l+h)>>1

            if(m==0 or m==(len(nums)-1)  or (l==h)):
                return nums[m]

            if(nums[m] == nums[m-1]):
                if(m%2==0):
                    h=m-2
                else:
                    l=m+1
            
            elif(nums[m] == nums[m+1]):
                if((m+1)%2 == 0):
                    h = m-1
                else:
                    l = m+2
            else:
                return nums[m]