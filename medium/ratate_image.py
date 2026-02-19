class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m1 = copy.deepcopy(matrix)
        n = len(matrix)
        for i in range(0,n):
            for j in range (0,n):
                matrix[j][n-i-1] = m1[i][j]
                