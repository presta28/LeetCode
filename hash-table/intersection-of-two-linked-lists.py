# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        sett=set()
        current=headA
        current1=headB
        while current is not None:
            sett.add(current)
            current=current.next
        while current1 is not None:
            if current1 in sett:
                return current1
            else:
                sett.add(current1)
                current1=current1.next
        return 
