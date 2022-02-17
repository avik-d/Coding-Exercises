# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if headA is None and headB is not None:
            return None
        if headA is not None and headB is None:
            return None
        
        if headA is headB:
            return headA
        
        len1 = 0
        len2 = 0
        
        cur1 = headA
        cur2 = headB
        
        while(cur1 is not None):
            cur1 = cur1.next
            len1 +=1
            
        while(cur2 is not None):
            cur2 = cur2.next
            len2 +=1
        
        cur1 = headA
        cur2 = headB
        
        diff=abs(len1-len2)
        i = 0
        
        if len1>len2:
            while i < diff:
                cur1 = cur1.next
                i = i + 1
        elif len1 < len2:
            while i<diff:
                cur2 = cur2.next
                i = i + 1
            
        
        while (cur1 is not None and cur2 is not None):
            if cur1 is cur2:
                return cur1
            cur1 = cur1.next
            cur2 = cur2.next
        return None
  
  
