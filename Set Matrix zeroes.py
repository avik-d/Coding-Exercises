#Algorithm
#Keep a note of if first row and first column has zero
#Then loop through the matrix - We can use first row and first column to store the information
#if matrix[i][j] is 0, we set matrix[i][0] to 0 and matrix[0][j] to 0
#Loop over the first row and first column to nullify rows and colums
#if matrix[i][0] is True, then nullify i th row
#if matrix[0][j] is true, nullify j th column

#Leetcode submission - https://leetcode.com/problems/set-matrix-zeroes/submissions/

class Solution:
    
    def nullifyrow(self,rowindex,colcount,matrix):
        for i in range(0,colcount):
            matrix[rowindex][i] = 0
            
    def nullifycol(self,colindex,rowcount,matrix):
        for i in range(0,rowcount):
            matrix[i][colindex] = 0       
            
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rowcount = len(matrix)
        colcount = len(matrix[0])
        
        
        #Check if first row or first col has zero
        firstrowhaszero = False
        firstcolhaszero= False
        for i in range(0,colcount):
            if matrix[0][i] is 0:
                firstrowhaszero = True
                break
        for i in range(0,rowcount):
            if matrix[i][0] is 0:
                firstcolhaszero=True
                break
                
        
        # Loop over the rest of the matrix and mark the first row and first col
        for i in range(1,rowcount):
            for j in range(1,colcount):
                if matrix[i][j] is 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
                    
        
        #nullify the rows and columns
        #vERY VERY IMPORTANT - The loop should start from 1 !!!!
        for i in range(1,rowcount):
            if matrix[i][0] is 0:
                self.nullifyrow(i,colcount,matrix)
        for i in range(1,colcount):
            if matrix[0][i] is 0:
                self.nullifycol(i,rowcount,matrix)
                
                
        #Check and nullify first row and first column if necessary
        if firstrowhaszero is True:
            self.nullifyrow(0,colcount,matrix)
        if firstcolhaszero is True:
            self.nullifycol(0,rowcount,matrix)
        
        
