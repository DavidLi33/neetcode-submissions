# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        right = dummy
        left = head
        while n:
            # Creates gap between left and right n, with dummy gap is n-1
            left = left.next
            n -= 1
        while left:
            right = right.next
            left = left.next
        right.next = right.next.next
        return dummy.next