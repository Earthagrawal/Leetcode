
nums=[1,12]
asd  = input()
k=7

i=0
summ=nums[0]
size=1
n=len(nums)
while((i<n-1) and (summ<k)):
    if(nums[i]==nums[i+1]):
        summ=nums[i+1]
        size=1
    
    else:
        if(nums[i+1]>k):
            print(1)
        else:
            print(summ, "  ", nums[i+1])
            summ = summ + nums[i+1]
            size+=1
            print(summ, "  ", nums[i+1])

    i+=1
if(summ>=k):
    print(size) 
else:
    print(-1)
