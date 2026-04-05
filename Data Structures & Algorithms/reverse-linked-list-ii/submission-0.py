# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        leftTail, curr = dummy, head
        for _ in range(left - 1):
            leftTail = curr
            curr = curr.next

        # reverse
        prev = None
        for _ in range(right - left + 1):
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        leftTail.next.next = curr
        leftTail.next = prev
        return dummy.next        