# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None      #checks if head is not empty

        newHead = head      
        if head.next:        #checks if the list has ended
            newHead = self.reverseList(head.next)    #sets the last node as the new head
            head.next.next = head                #sets the next node pointer to the current node
        head.next = None                          #sets the current nodes ponter to null (tail of the new list)
    
        return newHead

        
