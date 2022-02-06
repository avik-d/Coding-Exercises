# Definition for singly-linked list.

#https://leetcode.com/problems/merge-k-sorted-lists/

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        head = cur = None
        myheap=[]
        listCount = len(lists)
        
        # Build a heap of first element from every list
        # This should be O(k)
        for i in range(listCount):
            if lists[i] is not None:
                myheap.append((lists[i].val,i))
        heapify(myheap)
        
        #Pop an element
        #push on to the return list
        #Get the next element from the same list from where the element is popped
        
        while myheap:
            curval,id = heappop(myheap)
            newNode = ListNode(curval)
            if head is None:
                head = newNode
                cur = head
            else:
                cur.next = newNode
                cur = cur.next
                
            if lists[id].next is not None:
                heappush(myheap,(lists[id].next.val,id))
                lists[id] = lists[id].next
        
        return head
