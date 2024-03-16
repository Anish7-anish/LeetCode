# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse(self,l1: Optional[ListNode]):
        
        prev=None
        curr=l1

        while(curr):
            next_node=curr.next
            curr.next=prev
            prev=curr
            curr=next_node
        return prev


    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode()
        curr=dummy
        carry=0

        print(l1)
        print(l2)
        l1=self.reverse(l1)
        l2=self.reverse(l2)
        
        while(l1 or l2 or carry):
            v1=l1.val if l1 else 0
            v2=l2.val if l2 else 0

            val=v1+v2+carry

            carry=val//10
            val=val%10

            curr.next=ListNode(val)

            curr=curr.next
            l1=l1.next if l1 else None
            l2=l2.next if l2 else None
        return self.reverse(dummy.next)

        


        