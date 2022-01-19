#Algorithm:
1. Created a visited array
2. While there are unvisited elements, call DFS
3. Now mark the item visited.
4. Check all neighbors, if any of them is unvisited, call DFS from there.
5. Now when are back in the main function, that means we have covered all the nodes that we could traverse from the initial node.
6. This marks one island

# Leetcode link:
#https://leetcode.com/problems/number-of-islands/submissions/

class Solution:
    def mydfs(self,grid,visit,r,c,rows,cols):
        visit.add((r, c))
        if ((r>=0) and (r<rows) and (c-1>=0) and (c-1<cols) and ((r,c-1) not in visit) and (grid[r][c-1] == "1")):
            self.mydfs(grid,visit,r,c-1,rows,cols)
        if ((r-1>=0) and (r-1<rows) and (c>=0) and (c<cols) and ((r-1,c) not in visit) and (grid[r-1][c] == "1")):
            self.mydfs(grid,visit,r-1,c,rows,cols)
        if ((r+1>=0) and (r+1<rows) and (c>=0) and (c<cols) and ((r+1,c) not in visit) and (grid[r+1][c] == "1")):
            self.mydfs(grid,visit,r+1,c,rows,cols)
        if ((r>=0) and (r<rows) and (c+1>=0) and (c+1<cols) and ((r,c+1) not in visit) and (grid[r][c+1] == "1")):
            self.mydfs(grid,visit,r,c+1,rows,cols)

    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        if rows is 0:
            return 0
        cols = len(grid[0])
        visited = set()
        count = 0
        for i in range(0,rows):
            for j in range(0,cols):
                if (i,j)  not in visited:
                    if grid[i][j] == "1":
                        count = count + 1
                        self.mydfs(grid,visited,i,j,rows,cols)
        
        return count
