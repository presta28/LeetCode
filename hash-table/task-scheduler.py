class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        queue = []
        front = 0

        dictt = {}
        heap = []
        time = 0

        # Frequency count
        for alp in tasks:
            if alp not in dictt:
                dictt[alp] = 1
            else:
                dictt[alp] += 1

        # Build heap
        for task in dictt:
            heap.append([dictt[task], task])

        # Max Heapify Down
        def heapify_down(i):
            while True:
                left = 2 * i + 1
                right = 2 * i + 2

                if left >= len(heap):
                    break

                larger = left

                if right < len(heap) and heap[right][0] > heap[left][0]:
                    larger = right

                if heap[larger][0] <= heap[i][0]:
                    break

                temp = heap[i]
                heap[i] = heap[larger]
                heap[larger] = temp

                i = larger

        # Max Heapify Up
        def heapify_up(i):
            while i > 0:
                parent = (i - 1) // 2

                if heap[parent][0] >= heap[i][0]:
                    break

                temp = heap[parent]
                heap[parent] = heap[i]
                heap[i] = temp

                i = parent

        # Build Max Heap
        i = len(heap) // 2 - 1

        while i >= 0:
            heapify_down(i)
            i -= 1

        # Simulation
        while len(heap) > 0 or front < len(queue):

            # Move cooled-down tasks back to heap
            while front < len(queue) and queue[front][2] <= time:
                item = queue[front]
                front += 1

                heap.append([item[0], item[1]])
                heapify_up(len(heap) - 1)

            # If a task is available
            if len(heap) > 0:

                root = heap[0]

                # Remove root
                last = heap[len(heap) - 1]
                heap.pop()

                if len(heap) > 0:
                    heap[0] = last
                    heapify_down(0)

                remaining = root[0] - 1
                task = root[1]

                # Put task in cooldown
                if remaining > 0:
                    queue.append([
                        remaining,
                        task,
                        time + n + 1
                    ])

                time += 1

            # No task available → jump directly
            else:
                time = queue[front][2]

        return time