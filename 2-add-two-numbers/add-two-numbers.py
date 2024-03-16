# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        a=[]
        b=[]
        while(l1):
            a.append(l1.val)
            l1=l1.next
        while(l2):
            b.append(l2.val)
            l2=l2.next
        a=a[::-1]
        b=b[::-1]
        s = [str(i) for i in a]
        res1 = int("".join(s))
        s = [str(i) for i in b]
        res2 = int("".join(s))

        print(res1)
        print(res2)
        ans=list(str(res1+res2)[::-1])
        ans=[int(i) for i in ans] 
        l3=ListNode()
        head = l3
        head.val = ans[0]       
        for i in range(1, len(ans)):
            node = ListNode()
            node.val = ans[i]
            head.next = node
            head = head.next
        return l3
        

            
        
        



