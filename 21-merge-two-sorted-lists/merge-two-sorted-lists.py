# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy=prev=ListNode(-1)
        dummy.next=list1
        n1=list1
        n2=list2

        print(dummy)
        print(n1)
        
        print(n2)
        
        

        if not list1: return list2
        if not list2: return list1

        while n1 and n2:
            if n2.val>n1.val:
                if not n1.next:
                    n1.next=n2
                    break
                prev=n1
                n1=n1.next
            else:
                tmp=n2.next
                prev.next=n2
                n2.next=n1
                prev=n2
                n2=tmp
        return dummy.next

            







        
        