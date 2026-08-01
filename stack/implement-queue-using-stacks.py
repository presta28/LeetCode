class MyQueue:

    def __init__(self):
        self.input_stack = []
        self.output_stack = []
        self.size = 0

    def push(self, x: int) -> None:
        self.input_stack.append(x)
        self.size = self.size + 1

    def pop(self) -> int:

        if len(self.output_stack) == 0:

            while len(self.input_stack) > 0:
                value = self.input_stack.pop()
                self.output_stack.append(value)

        if self.size == 0:
            return -1

        removed_element = self.output_stack.pop()
        self.size = self.size - 1

        return removed_element

    def peek(self) -> int:

        if len(self.output_stack) == 0:

            while len(self.input_stack) > 0:
                value = self.input_stack.pop()
                self.output_stack.append(value)

        if self.size == 0:
            return -1

        return self.output_stack[-1]

    def empty(self) -> bool:

        if self.size == 0:
            return True

        return False

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()