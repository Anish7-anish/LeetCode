# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        d = ListNode()
        d.next = head
        dummy = d
        curr = d

        for i in range(n):
            curr = curr.next
        
        while curr!=None and curr.next!=None:
            dummy = dummy.next
            curr = curr.next
        dummy.next = dummy.next.next

        return d.next

        
        