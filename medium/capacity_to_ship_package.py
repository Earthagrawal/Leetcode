class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:

        def tellsDays(n):

            d = 1
            summ = 0
            for i in weights:
                if ((summ + i) <= n) :
                    summ += i
                else:            
                    d += 1
                    summ = i

            return d <= days

        left = max(weights)
        right = sum(weights)

        while left < right:        

            mid = (left + right) // 2

            if tellsDays(mid):
                right = mid
            else:
                left = mid + 1

        return left
