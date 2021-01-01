class ListNode:
     def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        merge =temp = ListNode(0)
        
        print(l1)
        
        while l1 != None or l2 != None:
            if l1 == None and l2 != None:
    
                temp.next = ListNode(l2.val)
                temp = temp.next
                l2 = l2.next
            
            elif l1 != None and l2 == None:
        
                temp.next = ListNode(l1.val)
                temp = temp.next
                l1 = l1.next
                     
            elif l1.val < l2.val:
           
                temp.next = ListNode(l1.val)
                temp = temp.next
                l1 = l1.next
            else:
                temp.next=ListNode(l2.val)
                temp = temp.next
                l2 = l2.next
                
        return merge.next