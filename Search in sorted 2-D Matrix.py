https://leetcode.com/problems/search-a-2d-matrix/submissions/
  
  
  class Solution:
    def myfunc(self,matrix,low,high,target,colCount):
        if low > high:
            return False
        mid = (low+high)//2
        if matrix[mid//colCount][mid%colCount] == target:
            return True
        if matrix[mid//colCount][mid%colCount] > target:
            return self.myfunc(matrix,low,mid-1,target,colCount)
        return self.myfunc(matrix,mid+1,high,target,colCount)
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rowCount = len(matrix)
        if rowCount == 0:
            return False
        colCount = len(matrix[0])
        total_no_of_elements = rowCount * colCount
        return self.myfunc(matrix,0,total_no_of_elements-1,target,colCount)
