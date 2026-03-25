class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:

        naturalnos = [ i  for i in range(1,2001)]
        for i in arr :
            naturalnos.remove(i)
        
        return naturalnos[k-1]