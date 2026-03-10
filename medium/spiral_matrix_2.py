class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [ [ 0 for i in range (0,n)] for i in range (0,n)]
        top,right,bottom,left = 0,n,n,0
        num = 1

        while(top<bottom and left<right and num<=(n*n)):
            for i in range(left,right):
                matrix[top][i]= num
                num +=1
            
            top+=1
            if(top== bottom or left == right): 
                break
            
            for i in range(top,bottom):
                matrix[i][right-1] = num
                num+=1
            right-=1

            if(top== bottom or left == right):
                break
  
            for i in range(right-1,left-1, -1):
                matrix[bottom-1][i] = num
                num+=1
            bottom-=1

            if(top== bottom or left == right):
                break

            for i in range(bottom-1, top-1, -1):
                matrix[i][left] = num
                num+=1

            left+=1

            if(top== bottom or left == right):
                break
        
        return matrix
            
            

