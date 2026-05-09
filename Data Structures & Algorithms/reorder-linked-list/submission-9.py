# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # First node in second half
        curr = slow.next
        # Cut off first half of matrix
        slow.next = prev = None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        # Prev new head second half
        l1 = head
        l2 = prev
        while l1 and l2:
            temp_1 = l1.next
            temp_2 = l2.next
            l1.next = l2
            l2.next = temp_1
            l1 = temp_1
            l2 = temp_2




            
        
