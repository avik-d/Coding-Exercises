https://leetcode.com/problems/linked-list-cycle/submissions/


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if head is None:
            return False
        
        if head.next is None:
            return False;
        
        first = head
        second = head
        
        
        while(first is not None and second is not None):
            
            if first.next:
                first = first.next;
            else:
                return False
            if second.next:
                second = second.next.next;
            else:
                return False
            if (first is second):
                return True
        return False
        
