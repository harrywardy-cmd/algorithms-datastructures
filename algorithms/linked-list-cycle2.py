class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Initialize two pointers at the head of the linked list
        # Slow moves one step at a time, fast moves two steps at a time
        slow, fast = head, head

        # Continue while there are enough nodes for the fast pointer
        while fast and fast.next:
            # Move the slow pointer forward by one node
            slow = slow.next

            # Move the fast pointer forward by two nodes
            fast = fast.next.next

            # If the two pointers meet, a cycle exists
            if slow == fast:
                return True

        # If the fast pointer reaches the end of the list,
        # there is no cycle
        return False
