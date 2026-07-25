# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# class Solution:
#     def hasCycle(self, head: Optional[ListNode]) -> bool:
#         sett=set()
#         if head==None:
#             return False
#         current=head
#         while current.next is not None:
#             if current in sett:
#                 return True
#             sett.add(current)
#             current =current.next
#         return False

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        current = head
        fast=head
        while fast is not None and fast.next is not None:
            if fast.next==None or fast.next.next==None:
                return False
            slow=slow.next
            fast = fast.next.next
            if slow==fast:
                return True
            