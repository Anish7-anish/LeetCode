class MinStack:

    def __init__(self):
        self.stk = []
        self.minn_stk = []

    def push(self, val: int) -> None:
        self.stk.append(val)

        if not self.minn_stk:
            self.minn_stk.append(val)
        elif self.minn_stk[-1] < val:
            self.minn_stk.append(self.minn_stk[-1])
        else:
            self.minn_stk.append(val)
        
    def pop(self) -> None:
        self.stk.pop()
        self.minn_stk.pop()

    def top(self) -> int:
        return self.stk[-1]

    def getMin(self) -> int:
        return self.minn_stk[-1]

        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()