class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = []

        # Add initial numbers
        for num in nums:
            self.add(num)

    def heapify_up(self, i):
        while i > 0:
            parent = (i - 1) // 2

            # Min Heap property already correct
            if self.heap[parent] <= self.heap[i]:
                break

            temp = self.heap[parent]
            self.heap[parent] = self.heap[i]
            self.heap[i] = temp

            i = parent

    def heapify_down(self, i):
        while True:
            left = 2 * i + 1
            right = 2 * i + 2

            if left >= len(self.heap):
                break

            smaller = left

            if right < len(self.heap):
                if self.heap[right] < self.heap[left]:
                    smaller = right

            # Min Heap property already correct
            if self.heap[i] <= self.heap[smaller]:
                break

            temp = self.heap[i]
            self.heap[i] = self.heap[smaller]
            self.heap[smaller] = temp

            i = smaller

    def add(self, val: int) -> int:

        # Heap is not full
        if len(self.heap) < self.k:
            self.heap.append(val)

            # New element is at the last index
            self.heapify_up(len(self.heap) - 1)

        # Heap is full
        else:
            # New value is better than current kth largest
            if val > self.heap[0]:
                self.heap[0] = val
                self.heapify_down(0)

        # Kth largest doesn't exist yet
        if len(self.heap) < self.k:
            return -1

        return self.heap[0]
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)