# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if l1 is None or l2 is None:
            return l1 or l2
        fake_head = ListNode(-1)
        curr1, curr2, curr = l1, l2, fake_head
        carry = 0
        while curr1 or curr2:
            if curr1 is None:
                val = curr2.val + carry
                curr2 = curr2.next
            elif curr2 is None:
                val = curr1.val + carry
                curr1 = curr1.next
            else:
                val = curr1.val + curr2.val + carry
                curr1 = curr1.next
                curr2 = curr2.next
            curr.next = ListNode(val % 10)
            carry = val // 10
            curr = curr.next
        if carry:
            curr.next = ListNode(carry)
        return fake_head.next