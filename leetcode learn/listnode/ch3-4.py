# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        valnukidashitehozon = []
        
        while head:
            valnukidashitehozon.append(head.val)
            head = head.next
        if len(valnukidashitehozon) == 0 or len(valnukidashitehozon) == 1:
            return True
        return valnukidashitehozon == valnukidashitehozon[::-1]