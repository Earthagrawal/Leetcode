class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res=[]
        top = 0
        bottom = len(matrix)
        left = 0
        right = len(matrix[0])

        while( top<bottom  and left<right):

            for i in range(left, right, 1 ):
                res.append(matrix[top][i])
            top+=1

            if(top>=bottom):
                return res

            for i in range( top , bottom,1):
                res.append(matrix[i][right-1])
            right-=1

            if(left>=right):
                return res

            for i in range( right-1, left-1, -1 ):
                res.append(matrix[bottom-1][i])
            bottom-=1

            if(top>=bottom):
                return res

            for i in range( bottom-1, top-1 , -1):
                res.append(matrix[i][left])
            left+=1

        return res


        