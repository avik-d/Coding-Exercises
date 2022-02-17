https://leetcode.com/problems/reverse-linked-list/submissions/
  
  
  # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        
        prev = None
        cur = head
        nextp = head.next
        
        
        while (cur is not None):
            cur.next = prev
            prev = cur
            cur = nextp
            if nextp is not None:
                nextp = nextp.next
            else:
                break
        return prev
        
