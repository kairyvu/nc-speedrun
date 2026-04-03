# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        def getGcd(num1, num2):
            while num2:
                num1, num2 = num2, num1 % num2
            return num1
        
        prev, curr = head, head.next
        while curr:
            gcd = getGcd(prev.val, curr.val)
            newNode = ListNode(gcd)
            prev.next = newNode
            newNode.next = curr
            prev = curr
            curr = curr.next
        return head