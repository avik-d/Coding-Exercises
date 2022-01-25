#https://leetcode.com/explore/interview/card/top-interview-questions-hard/118/trees-and-graphs/845/


class Solution(object):
    def myfunc(self,root,maxval):
        if root is None:
            return 0
        
        l = self.myfunc(root.left,maxval)
        r = self.myfunc(root.right, maxval)
        
        #We need to check maximum of 4 things and set maxval
        val1 = root.val
        val2 = val1 + l
        val3 = val1 + r
        val4 = val1 + l + r
        maxval[0] = max(val1,val2,val3,val4,maxval[0])
        
        #But we should only check 3 things for returning
        return max(val1, val2, val3)
    
    def maxPathSum(self, root):
        maxval = [-99999]
        self.myfunc(root,maxval)
        return maxval[0]
        
