# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        ans = head
        if head == None:
            return None
        elif head.val == val and head.next == None:
            return None

        while head != None:
            if head.val == val:
                head = head.next
                ans = head
            elif head.next == None:
                return ans
            elif head.next.val == val and head.next.next != None:             
                head.next = head.next.next
            elif head.next.val == val and head.next.next ==None:
                head.next = None
            else:
                head = head.next

        
        return ans