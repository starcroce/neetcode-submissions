# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        curr = head
        for _ in range(k):
            if curr is None:
                return head
            curr = curr.next
        new_head = self._reverse(head, curr)
        head.next = self.reverseKGroup(curr, k)
        return new_head

    def _reverse(self, head, tail):
        prev, curr = tail, head
        while curr != tail:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev