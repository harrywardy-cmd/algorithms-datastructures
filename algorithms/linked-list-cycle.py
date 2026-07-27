class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Start traversing from the head of the linked list
        curr = head

        # Store visited nodes in a set
        # If we encounter the same node again, a cycle exists
        seen = set()

        # Traverse the linked list until we reach the end
        while curr:
            # If the current node has already been visited,
            # we've found a cycle
            if curr in seen:
                return True

            # Mark the current node as visited
            seen.add(curr)

            # Move to the next node
            curr = curr.next

        # If we reach None, the list ends normally,
        # so there is no cycle
        return False
