# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        extra = 0
        dummyHead = ListNode(0)
        curr = dummyHead

        while l1 and l2:
            total = l1.val + l2.val + extra
            value, extra = total % 10, total // 10
            newNode = ListNode(value)
            curr.next = newNode
            curr = curr.next
            l1 = l1.next
            l2 = l2.next
        
        while l1:
            total = l1.val + extra
            value, extra = total % 10, total // 10
            newNode = ListNode(value)
            curr.next = newNode
            curr = curr.next
            l1 = l1.next
        
        while l2:
            total = l2.val + extra
            value, extra = total % 10, total // 10
            newNode = ListNode(value)
            curr.next = newNode
            curr = curr.next
            l2 = l2.next
        
        if extra:
            curr.next = ListNode(1)
        
        return dummyHead.next