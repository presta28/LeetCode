# class Solution:
#     def topKFrequent(self, words: List[str], k: int) -> List[str]:

#         # Frequency
#         freq = {}

#         for word in words:
#             if word not in freq:
#                 freq[word] = 1
#             else:
#                 freq[word] += 1

#         # [word, frequency]
#         arr = []

#         for key, value in freq.items():
#             arr.append([key, value])

#         # First k elements
#         minheap = []

#         for i in range(k):
#             minheap.append(arr[i])

#         # ---------------- HEAPIFY DOWN ----------------
#         def heapify_down(i):
#             while True:
#                 left = 2 * i + 1
#                 right = 2 * i + 2

#                 if left >= len(minheap):
#                     break

#                 smaller = left

#                 # Choose weaker child
#                 if right < len(minheap):

#                     if minheap[right][1] < minheap[left][1]:
#                         smaller = right

#                     elif minheap[right][1] == minheap[left][1]:
#                         # Same frequency:
#                         # lexicographically larger word is weaker
#                         if minheap[right][0] > minheap[left][0]:
#                             smaller = right

#                 # Parent already weaker than child
#                 if minheap[i][1] < minheap[smaller][1]:
#                     break

#                 if (minheap[i][1] == minheap[smaller][1] and
#                     minheap[i][0] > minheap[smaller][0]):
#                     break

#                 temp = minheap[i]
#                 minheap[i] = minheap[smaller]
#                 minheap[smaller] = temp

#                 i = smaller

#         # ---------------- HEAPIFY UP ----------------
#         def heapify_up(i):
#             while i > 0:

#                 parent = (i - 1) // 2

#                 # Parent is already weaker
#                 if minheap[parent][1] < minheap[i][1]:
#                     break

#                 if (minheap[parent][1] == minheap[i][1] and
#                     minheap[parent][0] > minheap[i][0]):
#                     break

#                 temp = minheap[i]
#                 minheap[i] = minheap[parent]
#                 minheap[parent] = temp

#                 i = parent

#         # ---------------- BUILD MIN HEAP ----------------
#         i = (k // 2) - 1

#         while i >= 0:
#             heapify_down(i)
#             i -= 1

#         # ---------------- REMAINING ELEMENTS ----------------
#         for i in range(k, len(arr)):

#             # New word has higher frequency
#             if arr[i][1] > minheap[0][1]:

#                 minheap[0] = arr[i]
#                 heapify_down(0)

#             # Same frequency
#             elif arr[i][1] == minheap[0][1]:

#                 # Smaller word is better
#                 if arr[i][0] < minheap[0][0]:
#                     minheap[0] = arr[i]
#                     heapify_down(0)

#         # ---------------- ANSWER ----------------
#         answer = []

#         while len(minheap) > 0:

#             # Root = weakest among current elements
#             answer.append(minheap[0][0])

#             # Remove root
#             minheap[0] = minheap[len(minheap) - 1]
#             minheap.pop()

#             if len(minheap) > 0:
#                 heapify_down(0)

#         # Heap gives weakest -> strongest
#         # Reverse manually
#         left = 0
#         right = len(answer) - 1

#         while left < right:
#             temp = answer[left]
#             answer[left] = answer[right]
#             answer[right] = temp

#             left += 1
#             right -= 1

#         return answer

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:

        # ---------------- FREQUENCY MAP ----------------
        freq = {}

        for word in words:
            if word not in freq:
                freq[word] = 1
            else:
                freq[word] += 1

        # ---------------- MIN HEAP ----------------
        heap = []

        # Returns True if a should come BEFORE b
        # according to our "weakest first" heap ordering
        def weaker(a, b):
            # a and b = [word, frequency]

            if a[1] < b[1]:
                return True

            if a[1] == b[1] and a[0] > b[0]:
                return True

            return False

        # ---------------- HEAPIFY DOWN ----------------
        def heapify_down(i):
            while True:
                left = 2 * i + 1
                right = 2 * i + 2

                if left >= len(heap):
                    break

                weaker_child = left

                if right < len(heap):
                    if weaker(heap[right], heap[left]):
                        weaker_child = right

                # If parent is already weaker than/equal in heap order
                # then heap property is correct
                if not weaker(heap[weaker_child], heap[i]):
                    break

                temp = heap[i]
                heap[i] = heap[weaker_child]
                heap[weaker_child] = temp

                i = weaker_child

        # ---------------- HEAPIFY UP ----------------
        def heapify_up(i):
            while i > 0:
                parent = (i - 1) // 2

                if not weaker(heap[i], heap[parent]):
                    break

                temp = heap[i]
                heap[i] = heap[parent]
                heap[parent] = temp

                i = parent

        # ---------------- PROCESS UNIQUE WORDS ----------------
        for word in freq:
            current = [word, freq[word]]

            # Heap not full
            if len(heap) < k:
                heap.append(current)
                heapify_up(len(heap) - 1)

            # Heap full
            else:
                # Is current word better than weakest word?
                if weaker(heap[0], current):
                    heap[0] = current
                    heapify_down(0)

        # ---------------- EXTRACT K WORDS ----------------
        # Heap itself is NOT sorted.
        # We need answer in correct order.

        answer = []

        while len(heap) > 0:

            # Root = weakest among remaining
            word = heap[0][0]

            answer.append(word)

            # Remove root
            heap[0] = heap[len(heap) - 1]
            heap.pop()

            if len(heap) > 0:
                heapify_down(0)

        # We extracted weakest -> strongest,
        # so reverse manually.
        left = 0
        right = len(answer) - 1

        while left < right:
            temp = answer[left]
            answer[left] = answer[right]
            answer[right] = temp

            left += 1
            right -= 1

        return answer