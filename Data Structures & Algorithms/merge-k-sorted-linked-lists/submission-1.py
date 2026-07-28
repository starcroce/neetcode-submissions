# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import heapq

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None
        heap = []
        cnt = 0
        for l in lists:
            if l:
                heapq.heappush(heap, (l.val, cnt, l))
                cnt += 1
        fake_head = ListNode(-1)
        curr = fake_head
        while len(heap):
            _, _, temp = heapq.heappop(heap)
            curr.next = temp
            temp = temp.next
            if temp:
                heapq.heappush(heap, (temp.val, cnt, temp))
                cnt += 1
            curr = curr.next
        return fake_head.next