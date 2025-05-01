class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []
        self.min = float("inf")
    def push(self, val: int) -> None:
        if not self.stack:
            self.min = val
        elif val < self.min:
            self.min = val
        self.stack.insert(0,val)
        self.min_stack.insert(0,self.min)

    def pop(self) -> None:
        self.stack.pop(0)
        self.min_stack.pop(0)
        if self.min_stack:
            self.min = self.min_stack[0]

    def top(self) -> int:
        return self.stack[0]

    def getMin(self) -> int:
        return self.min_stack[0]
        
