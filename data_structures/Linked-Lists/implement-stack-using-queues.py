class MyStack:

    def __init__(self):
        self.q = deque()

    def push(self, x: int) -> None:
        self.q.append(x) # add to the top of the stack
        

    def pop(self) -> int:
        for i in range(len(self.q)-1):      #will pop the bottom of the stack then push to the top untill x is now at the bottom of the stack
            self.push(self.q.popleft())
        return self.q.popleft()             #return pop 
        

    def top(self) -> int:
        return self.q[-1]   #return the top of the stack

    def empty(self) -> bool:
        return len(self.q) == 0 #check if stack is empty 
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
