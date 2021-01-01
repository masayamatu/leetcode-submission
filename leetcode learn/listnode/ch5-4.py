"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if head == None:
            return None
        
        temp1 = head
        
        while temp1:
            copy = Node(temp1.val)
            copy.next = temp1.next
            temp1.next = copy
            temp1 = copy.next
            
        temp1 = head
        temp2 = temp1.next
        
        while temp1:
            temp2.random = temp1.random.next if temp1.random else None
            temp1 = temp2.next
            temp2 = temp1.next if temp1 else None
        temp1 = head
        temp2 = copy = head.next
        while temp1:
            temp1.next = temp2.next
            temp1 = temp1.next
            if temp1:
                temp2.next = temp1.next
                temp2 = temp2.next
        return copy