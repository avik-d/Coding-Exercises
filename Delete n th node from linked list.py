https://leetcode.com/problems/delete-node-in-a-linked-list/submissions/
  
  class Solution:
    def deleteNode(self, node):
        node.val = node.next.val
        node.next = node.next.next
