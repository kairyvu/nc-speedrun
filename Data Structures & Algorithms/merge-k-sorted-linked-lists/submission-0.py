# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None
        
        def mergeLists(l1, l2):
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
        
        while len(lists) >= 2:
            l1, l2 = lists.pop(), lists.pop()
            lists.append(mergeLists(l1, l2))
        
        return lists[0]