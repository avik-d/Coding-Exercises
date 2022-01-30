https://leetcode.com/problems/unique-paths/submissions/
  
  class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        ways = [[0 for j in range(n)] for i in range(m)]

        #There's only one way to reach any element on first row / first column
        for i in range(m):
            ways[i][0]=1
        for j in range(n):
            ways[0][j]=1
            
        for i in range(1,m):
            for j in range(1,n):
                ways[i][j] = ways[i][j-1]+ways[i-1][j]
                
        return ways[m-1][n-1]
        
            
        
