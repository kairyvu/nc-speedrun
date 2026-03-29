# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def divide(self, lists, l, r):
        if l > r:
            return None
        if l == r:
            return lists[l]
        
        mid = (l + r) // 2
        left = self.divide(lists, l, mid)
        right = self.divide(lists, mid + 1, r)
        return self.mergeLists(left, right)

    def mergeLists(self, l1, l2):
        dummyHead = ListNode()
        curr = dummyHead

        while l1 or l2:
            l1Val = l1.val if l1 else float("inf")
            l2Val = l2.val if l2 else float("inf")

            if l1Val <= l2Val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next
        return dummyHead.next

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None
        return self.divide(lists, 0, len(lists) - 1)
        