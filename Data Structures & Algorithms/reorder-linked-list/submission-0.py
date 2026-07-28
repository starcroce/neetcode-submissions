# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if head is None or head.next is None:
            return
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        head1, head2 = head, slow.next
        slow.next = None
        head2 = self._reverse(head2)

        fake_head = ListNode(-1)
        curr, idx = fake_head, 0
        while head1 and head2:
            if idx % 2 == 0:
                curr.next = head1
                head1 = head1.next
            else:
                curr.next = head2
                head2 = head2.next
            curr = curr.next
            idx += 1
        curr.next = head1 or head2

    def _reverse(self, head):
        prev, curr = None, head
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev