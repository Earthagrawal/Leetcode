class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if m * k >len(bloomDay):
            return -1


        def check(n):
            sum,res=0,0
            print()
            i=0
            while (i < len(bloomDay)):

                if(bloomDay[i] <= n):
                    res+=1
                else:
                    sum += res//k
                    res=0
                i+=1

            sum += res//k
            return sum
        
        left = min(bloomDay)
        right = max(bloomDay)
        ans= right
        target = m*k

        while(left <= right): 
            mid = left + ( right-left )//2

            res = check(mid)
            print("what we got back for ", mid, " is: ", res)   
            if(res >= m ):
                ans = mid
                right = mid-1
            else:
                left = mid+1

        return ans