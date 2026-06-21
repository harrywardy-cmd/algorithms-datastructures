# Node class for the doubly linked list
class ListNode:
    def __init__(self, val, prev=None, next=None):
        # Store the current webpage URL
        self.val = val

        # Reference to the previous page in history
        self.prev = prev

        # Reference to the next page in history
        self.next = next


class BrowserHistory:

    def __init__(self, homepage: str):
        """
        Initialize browser history with the homepage.

        A doubly linked list is used to allow efficient
        backward and forward navigation.
        """
        self.cur = ListNode(homepage)

    def visit(self, url: str) -> None:
        """
        Visit a new URL.

        Any forward history is discarded because the new page
        becomes the latest page in the browsing path.
        """

        # Create a new node and connect it to the current page
        self.cur.next = ListNode(url, self.cur)

        # Move the current pointer to the newly visited page
        self.cur = self.cur.next

    def back(self, steps: int) -> str:
        """
        Move backward through browser history up to 'steps' times.

        Stops early if there are no more previous pages.
        """

        while self.cur.prev and steps > 0:
            # Move to the previous page
            self.cur = self.cur.prev
            steps -= 1

        # Return the URL of the current page
        return self.cur.val

    def forward(self, steps: int) -> str:
        """
        Move forward through browser history up to 'steps' times.

        Stops early if there are no more forward pages.
        """

        while self.cur.next and steps > 0:
            # Move to the next page
            self.cur = self.cur.next
            steps -= 1

        # Return the URL of the current page
        return self.cur.val

        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
