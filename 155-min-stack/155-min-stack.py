class MinStack:

    def __init__(self):
        self.stack = list()
        self.count = 0

    def push(self, val: int) -> None:
        if self.count == 0:
            self.stack.append((val, val))
        else:
            prev, prev_min = self.stack.pop()
            nxt_min = prev_min
            if val < nxt_min:
                nxt_min = val
            self.stack.append((prev, prev_min))
            self.stack.append((val, nxt_min))
        
        self.count += 1
        

    def pop(self) -> None:
        if self.count != 0:
            pop_val, pop_min = self.stack.pop()
            self.count -= 1
            return pop_val

    def top(self) -> int:
        if self.count != 0:
            top_val, top_min = self.stack.pop()
            self.stack.append((top_val, top_min))
            return top_val
        return -1
        

    def getMin(self) -> int:
        if self.count != 0:
            top_val, top_min = self.stack.pop()
            self.stack.append((top_val, top_min))
            return top_min
        return -1
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()