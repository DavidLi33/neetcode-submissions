# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        left = dummy
        right = head

        while n > 0:            #Advance n nodes from start
            right = right.next
            n -= 1 
        
        while right:            #Ensure a gap of n nodes
            left = left.next    #At node we want to delete
            right = right.next  #However we want to be at the node before, 
                                #which is why we use the dummy node
        left.next = left.next.next  #Skips over the node
        return dummy.next