# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy

        carry_num = 0
        while l1 or l2 or carry_num:
            v1, v2 = l1.val if l1 else 0, l2.val if l2 else 0
            val = v1 + v2 + carry_num
            carry_num = val // 10
            ones = val % 10
            
            curr.next = ListNode(ones)
            curr = curr.next

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        
        return dummy.next
