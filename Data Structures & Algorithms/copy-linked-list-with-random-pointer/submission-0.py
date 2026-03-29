"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        curr = head

        while curr:
            newNode = Node(curr.val, curr.next)
            curr.next = newNode
            curr = newNode.next
        
        curr = head
        while curr and curr.next:
            if curr.random:
                curr.next.random = curr.random.next
            curr = curr.next.next
        
        newCurr, oldCurr = Node(0, head), head
        dummyNewHead = newCurr
        while oldCurr:
            newCurr.next = oldCurr.next
            newCurr = newCurr.next
            oldCurr.next = oldCurr.next.next
            oldCurr = oldCurr.next
        return dummyNewHead.next