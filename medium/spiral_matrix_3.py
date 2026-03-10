class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:

        r, c = rows, cols
        rs, cs = rStart, cStart

        matrix = [ [ 0 for i in range(0,3*r) ] for j in range(0,3*c) ]

        top, bottom = r+rs , r+rs
        left,right = c+cs, c+cs
        i,j = top,left

        res = [ [i-r,j-c]  ]

        while(len(res) < r*c):

            right+=1
            while(j<right):
                j+=1
                if( (0<=(i-rows)<rows) and ( 0<=(j-cols)<cols) ):
                    res.append([i-r,j-c])
            
            if(len(res) == r*c):
                break

            bottom+=1
            while(i<bottom):
                i+=1
                if( (0<=(i-rows)<rows) and ( 0<=(j-cols)<cols) ):
                    res.append([i-r,j-c])

            if(len(res) == r*c):
                break

            left-=1
            while(j>left):
                j-=1
                if( (0<=(i-rows)<rows) and ( 0<=(j-cols)<cols) ):
                    res.append([i-r,j-c])

            if(len(res) == r*c):
                break
            
            top-=1
            while(i>top):
                i-=1
                if( (0<=(i-rows)<rows) and ( 0<=(j-cols)<cols) ):
                    res.append([i-r,j-c])
        

        return res
        