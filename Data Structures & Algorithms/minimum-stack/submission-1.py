class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []
        

    def push(self, val: int) -> None:
        if self.stack != None:
            if self.minStack != None and len(self.minStack) > 0:
                if val < self.minStack[-1]:
                    self.minStack.append(val)
                else:
                    self.minStack.append(self.minStack[-1])
            else:
                self.minStack.append(val)

            self.stack.append(val)
        
        return None

    def pop(self) -> None:
        if self.stack != None and len(self.stack) > 0:
            self.stack.pop()
            self.minStack.pop()

        return None

    def top(self) -> int:
        if self.stack != None and len(self.stack) > 0:
            return self.stack[-1]

    def getMin(self) -> int:
        if self.stack != None and len(self.stack) > 0:
            return self.minStack[-1]

