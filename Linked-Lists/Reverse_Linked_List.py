# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev_node = None
        current_node = head


        while current_node != None:
            # save the next node 
            next_node = current_node.next
            #move the pointer to the previous node (this will detach the node, luckly we save the other nodes in next_node)
            current_node.next = prev_node
            # move up the previous node to the current node
            prev_node = current_node
            #move the current node to next one to move through the list
            current_node = next_node

        return prev_node

