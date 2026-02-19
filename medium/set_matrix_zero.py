import copy

matrix = [[1,1,1],[1,0,1],[1,1,1]]
       
m1 = copy.deepcopy( matrix)
m2 = copy.deepcopy( matrix)

n = len(m1)
m = len(m1[0])

for i in range (0,n) :
    for j in range (0,m):
        if(m1[i][j]==0):
            for k in range(0,m):
                m2[i][k]=0
            for k in range(0,n):
                m2[k][j]=0
        print(m2)
        print(m1)
        print()
        
#return m2
         

        