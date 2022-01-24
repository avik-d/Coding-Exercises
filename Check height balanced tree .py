https://leetcode.com/problems/balanced-binary-tree/submissions/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def myfunc(self,root,height):
        if root is None:
            height.append(0)
            return True
        lh = []
        rh = []
        l = self.myfunc(root.left,lh)
        r = self.myfunc(root.right,rh)
        
        height.append(max(lh[0],rh[0])+1)
        if l and r and abs(lh[0]-rh[0])<=1:
            return True
        return False
        
    def isBalanced(self, root: TreeNode) -> bool:
        height=[]
        return self.myfunc(root,height)
        
