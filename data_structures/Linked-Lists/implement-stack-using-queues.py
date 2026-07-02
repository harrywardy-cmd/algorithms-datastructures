from collections import deque

class MyStack:

    def __init__(self):
        # Use a queue (deque) as the underlying data structure.
        # Although a queue is FIFO, we will simulate LIFO stack behavior.
        self.q = deque()

    def push(self, x: int) -> None:
        # Add the new element to the back of the queue.
        # This represents pushing onto the top of the stack.
        self.q.append(x)

    def pop(self) -> int:
        # Rotate all elements except the last one.
        # Each front element is removed and added back to the end,
        # moving the newest element to the front of the queue.
        for i in range(len(self.q) - 1):
            self.push(self.q.popleft())

        # Remove and return the front element.
        # After the rotation above, this is the "top" of the stack.
        return self.q.popleft()

    def top(self) -> int:
        # Return the last element in the queue,
        # which represents the top of the stack.
        return self.q[-1]

    def empty(self) -> bool:
        # Return True if the queue contains no elements,
        # otherwise return False.
        return len(self.q) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
