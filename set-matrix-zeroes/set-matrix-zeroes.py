class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = len(matrix)
        cols = len(matrix[0])
        firstrowisZero = firstcolisZero = False
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c]==0:
                    if r==0:
                        firstrowisZero=True
                    if c==0:
                        firstcolisZero=True
                    matrix[r][0] = matrix[0][c] = 0
        
        for r in range(1,rows):
            for c in range(1,cols):
                matrix[r][c] = 0 if not matrix[r][0] or not matrix[0][c] else matrix[r][c]
        
        if firstrowisZero:
            for c in range(cols):
                matrix[0][c] = 0
        if firstcolisZero:
            for r in range(rows):
                matrix[r][0] = 0