 #https://leetcode.com/problems/rotate-image/submissions/
  
  class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        
        #Transpose the matrix
        for i in range(0,len(matrix)):
            for j in range(i,len(matrix)):
                if i is j:
                    continue
                else:
                    temp = matrix[i][j]
                    matrix[i][j] = matrix[j][i]
                    matrix[j][i] = temp
        
        #Reverse each row
        for i in range(0,len(matrix)):
            matrix[i].reverse()
        
