# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        length = 0
        temp = head
        tail = None
        while temp:
            tail = temp
            temp = temp.next
            length += 1
        if head == None or k == 0 or length==k:
            return head
        k %= length
        for i in range(length-k):
            tail.next = ListNode(head.val)
            tail = tail.next
            head = head.next
            print(tail)
            print(head)
        return head