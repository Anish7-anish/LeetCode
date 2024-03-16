# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        c=0
        dummy=head
        while(dummy):
            dummy=dummy.next
            c+=1
        if c==1:
            return None
        mid=c//2
        print(c,mid)
        

        curr=head
        
        k=0
        next_node=curr.next

        
        while(next_node):
            k+=1
            print(k)
            if k==mid:
                curr.next=next_node.next
                next_node=next_node.next
            else:
                curr=next_node
                next_node=next_node.next
        print(k)
        return head
        

        
