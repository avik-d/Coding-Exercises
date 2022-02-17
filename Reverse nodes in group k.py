https://leetcode.com/problems/reverse-nodes-in-k-group/submissions/
  
  # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        cur = head
        prev = None
        if head is not None:
            nextp = head.next
        count = 0
        
        #Count if there are at least k nodes before attempting to reverse
        nodecount = 0
        cur = head
        while(cur is not None):
            nodecount += 1
            cur = cur.next
        cur = head
            
        if  nodecount >= k:
            while(count<k and cur is not None):
                cur.next = prev
                prev = cur
                cur = nextp
                if nextp is not None:
                    nextp = nextp.next
                count += 1
            if cur is not None:
                head.next = self.reverseKGroup(cur,k)
            return prev
        else:
            return head
        
