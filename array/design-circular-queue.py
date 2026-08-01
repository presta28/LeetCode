class MyCircularQueue:

    def __init__(self, capacity: int):
        self.queue = [None] * capacity

        self.capacity = capacity
        self.front = 0
        self.rear = -1
        self.size = 0

    def enQueue(self, value: int) -> bool:

        if self.size == self.capacity:
            return False

        self.rear = (self.rear + 1) % self.capacity
        self.queue[self.rear] = value

        self.size = self.size + 1

        return True

    def deQueue(self) -> bool:

        if self.size == 0:
            return False

        self.front = (self.front + 1) % self.capacity
        self.size = self.size - 1

        return True

    def Front(self) -> int:

        if self.size == 0:
            return -1

        return self.queue[self.front]

    def Rear(self) -> int:

        if self.size == 0:
            return -1

        return self.queue[self.rear]

    def isEmpty(self) -> bool:

        if self.size == 0:
            return True

        return False

    def isFull(self) -> bool:

        if self.size == self.capacity:
            return True

        return False