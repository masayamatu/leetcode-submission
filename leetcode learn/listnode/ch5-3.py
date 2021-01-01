"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        if head == None:
            return None
        now = head
        nexthozonbox = []
        while now.next != None or now.child != None:
                if now.child != None:
                    if now.next != None:
                        nexthozonbox.append(now.next)
                    now.next = now.child
                    now.next.prev = now
                    now.child = None           
                now = now.next
        for i in reversed(nexthozonbox):
            now.next = i
            now.next.prev = now
            while now.next != None:
                now = now.next
        return head