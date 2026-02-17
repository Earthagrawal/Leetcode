class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        lp,ln = [],[]
        for i in nums:
            if(i<0):
                ln.append(i)
            else:
                lp.append(i)
            
        for i in range (0, len(lp)):
            nums[2*i] = lp[i]
            nums[2*i+1] = ln[i]
        

        return nums