# # Definition for singly-linked list.
# # class ListNode:
# #     def __init__(self, val=0, next=None):
# #         self.val = val
# #         self.next = next
    #solution 1
            # class Solution:
            #     def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
            #         len=0
            #         current=head
            #         while current.next is not None:
            #             len+=1
            #             current=current.next
            #         len+=1
            #         i=1
            #         current=head
            #         if len==n:
            #             return head.next
            #         while i<len-n:
            #             current=current.next
            #             i=i+1
            #         current.next=current.next.next
            #         return head
#solution 2 class Solution:
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        dummy = ListNode(0)
        dummy.next = head

        slow = dummy
        fast = dummy

        # Fast ko n steps aage bhejo
        for i in range(n):
            fast = fast.next

        # Gap maintain karte hue dono ko move karo
        while fast.next is not None:
            slow = slow.next
            fast = fast.next

        # Nth node from end remove karo
        slow.next = slow.next.next

        return dummy.next