# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        tail=dummy
        current1=list1
        current2=list2
        while current1 is not None and current2 is not None:
            if current1.val<=current2.val:
                tail.next=ListNode(current1.val)
                current1=current1.next
            else:
                tail.next=ListNode(current2.val)
                current2=current2.next
            tail=tail.next
        while current1 is not None:
            tail.next = ListNode(current1.val)
            tail = tail.next
            current1 = current1.next

        while current2 is not None:
            tail.next = ListNode(current2.val)
            tail = tail.next
            current2 = current2.next
        return dummy.next