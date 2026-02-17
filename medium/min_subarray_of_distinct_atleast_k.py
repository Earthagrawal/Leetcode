from collections import defaultdict
def minLength(nums, k):
    l,r=0,0
    summ=0
    result = float('inf')
    dict = defaultdict(int)

    while r<len(nums) :
        dict[nums[r]] +=1
        if dict[nums[r]] == 1 :
            summ += nums[r]
            
        
        while l<=r and summ>=k:
            print(dict)
            print(r," ",l," ")
            result = min(result , r-l+1)
            dict[nums[l]]-=1
            if dict[nums[l]] == 0 :
                summ -= nums[l]
            l+=1
            print(dict)
            print(result)
            print(summ)
       
        r+=1

    return result

x = minLength([5,5,4] , 5)
print(x)