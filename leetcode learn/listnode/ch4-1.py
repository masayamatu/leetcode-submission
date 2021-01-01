class Node:
    def __init__(self,val,next=None):
        self.val = val
        self.next = next
class MyLinkedList:

    def __init__(self,head = None):
        """
        Initialize your data structure here.
        """
        self.head = head
        self.length = 0
        

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        if index >= self.length:
            return -1
        else:
            cur_node = self.head
            cur_idx = 0
            while cur_idx in range(0,self.length):
                if cur_idx == index:
                    return cur_node.val
                cur_node = cur_node.next
                cur_idx += 1
       

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node
        self.length += 1
        return 
        
    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        new_node = Node(val)
        cur_node = self.head
        if self.head == None:
            self.head = new_node
            self.length += 1
            return
        while cur_node.next:
            cur_node = cur_node.next
        cur_node.next = new_node
        self.length += 1

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        if index > self.length:
            return
        elif index ==0:
            self.addAtHead(val)
        else:
            cur_node = self.head           
            prev_node = self.head
            cur_idx = 0
            while cur_idx != index:
                prev_node = cur_node
                cur_node = cur_node.next
                cur_idx += 1
            new_node = Node(val)
            prev_node.next = new_node
            new_node.next = cur_node
            self.length += 1

            return 
        

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        cur_node = self.head
        last_node = self.head
        if self.length <= index:
            return
        if index == 0:
            self.head = cur_node.next
        else:
            cur_idx = 0
            while cur_idx != index:
                last_node = cur_node
                cur_node = cur_node.next
                cur_idx += 1
            last_node.next = cur_node.next
            self.length -= 1
            return