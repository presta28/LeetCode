class MyStack:

    def __init__(self):
        self.input_queue = []
        self.output_queue = []
        self.front = 0

    def push(self, x: int) -> None:

        # New element sabse pehle temporary queue mein
        self.output_queue.append(x)

        # Main queue ke valid elements transfer karo
        while self.front < len(self.input_queue):

            value = self.input_queue[self.front]
            self.front = self.front + 1

            self.output_queue.append(value)

        # Temporary queue ko main queue bana do
        self.input_queue = self.output_queue
        self.output_queue = []

        # New main queue ka front index reset
        self.front = 0

    def pop(self) -> int:

        removed_value = self.input_queue[self.front]
        self.front = self.front + 1

        return removed_value

    def top(self) -> int:

        return self.input_queue[self.front]

    def empty(self) -> bool:

        if self.front == len(self.input_queue):
            return True

        return False

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()