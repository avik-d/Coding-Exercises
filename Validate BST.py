https://leetcode.com/problems/validate-binary-search-tree/submissions/
  

import sys
class Solution:
    def isval(self,root,leftval,rightval):
        if root is None:
            return True
        l = self.isval(root.left,leftval,root.val)
        r = self.isval(root.right,root.val,rightval )
        if l and r:
            if root.val > leftval and root.val < rightval:
                return True
        return False
        
        
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.isval(root,-sys.maxsize-1,sys.maxsize)
        
