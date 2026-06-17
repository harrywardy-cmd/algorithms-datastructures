# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Base case: if the list is empty, return None
        if not head:
            return None

        # Assume the current node is the new head initially
        newHead = head

        # If there is another node ahead,
        # continue recursively until we reach the tail
        if head.next:
            # Reverse the rest of the list and get the new head
            newHead = self.reverseList(head.next)

            # Reverse the pointer:
            # Example: 1 -> 2 becomes 1 <- 2
            head.next.next = head

        # Break the original forward link
        # Prevents cycles in the reversed list
        head.next = None

        # Return the head of the reversed list
        return newHead

        
