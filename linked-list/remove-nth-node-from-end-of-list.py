# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        len=0
        current=head
        while current.next is not None:
            len+=1
            current=current.next
        len+=1
        i=1
        current=head
        if len==n:
            return head.next
        while i<len-n:
            current=current.next
            i=i+1
        current.next=current.next.next
        return head
        