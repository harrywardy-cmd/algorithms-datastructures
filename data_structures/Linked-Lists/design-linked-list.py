class ListNode:        #     create a note with val and none on both pointers
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None

class MyLinkedList:

    def __init__(self):
        self.head = ListNode(0)    #    creates dummy nodes and connects them 
        self.tail = ListNode(0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, index: int) -> int:
        cur = self.head.next
        while cur and index > 0:    #    used to itterate through the linked list until it finds index
            cur = cur.next
            index -= 1
        if cur and cur != self.tail and index == 0: #     checks if the node is in bounds and the index is found
            return cur.val
        return -1

    def addAtHead(self, val: int) -> None: 
        node, next, prev = ListNode(val), self.head.next, self.head
        prev.next = node
        next.prev = node
        node.next = next
        node.prev = prev

    def addAtTail(self, val: int) -> None:
        node, next, prev = ListNode(val), self.tail, self.tail.prev
        prev.next = node
        next.prev = node
        node.next = next
        node.prev = prev

    def addAtIndex(self, index: int, val: int) -> None:
        cur = self.head.next
        while cur and index > 0:    #    used to itterate through the linked list until it finds index
            cur = cur.next
            index -= 1
        if cur and index == 0:    #     check if cur is valid
            node, next, prev = ListNode(val), cur, cur.prev
            prev.next = node
            next.prev = node
            node.next = next
            node.prev = prev


    def deleteAtIndex(self, index: int) -> None:
        cur = self.head.next
        while cur and index > 0:    #    used to itterate through the linked list until it finds index
            cur = cur.next
            index -= 1
        if cur and cur != self.tail and index == 0:  #     check if cur is valid
            next, prev = cur.next, cur.prev
            next.prev = prev
            prev.next = next
