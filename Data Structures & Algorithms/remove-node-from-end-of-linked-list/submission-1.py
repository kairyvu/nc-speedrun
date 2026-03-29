# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummyHead = ListNode()
        dummyHead.next = head

        curr = head
        for _ in range(n - 1):
            curr = curr.next
        prev = dummyHead

        while curr and curr.next:
            curr = curr.next
            prev = prev.next

        prev.next = prev.next.next
        return dummyHead.next