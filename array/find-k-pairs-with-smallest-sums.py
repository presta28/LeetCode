class Solution:
    def kSmallestPairs(self, nums1, nums2, k):
        
        heap = []
        ans = []

        # -------------------------
        # Heapify Up
        # -------------------------
        def heapify_up(i):
            while i > 0:
                parent = (i - 1) // 2

                if heap[parent][0] <= heap[i][0]:
                    break

                temp = heap[parent]
                heap[parent] = heap[i]
                heap[i] = temp

                i = parent

        # -------------------------
        # Heapify Down
        # -------------------------
        def heapify_down(i):
            while True:
                left = 2 * i + 1
                right = 2 * i + 2

                if left >= len(heap):
                    break

                smaller = left

                if right < len(heap) and heap[right][0] < heap[left][0]:
                    smaller = right

                if heap[i][0] <= heap[smaller][0]:
                    break

                temp = heap[i]
                heap[i] = heap[smaller]
                heap[smaller] = temp

                i = smaller

        # ---------------------------------
        # Initially: first pair of each row
        # ---------------------------------
        limit = len(nums1)

        if limit > k:
            limit = k

        for i in range(limit):
            heap.append([nums1[i] + nums2[0], i, 0])
            heapify_up(len(heap) - 1)

        # ---------------------------------
        # Extract k smallest candidates
        # ---------------------------------
        count = 0

        while len(heap) > 0 and count < k:

            # smallest candidate
            current = heap[0]

            total = current[0]
            i = current[1]
            j = current[2]

            ans.append([nums1[i], nums2[j]])
            count += 1

            # Remove root
            last = heap[len(heap) - 1]
            heap.pop()

            if len(heap) > 0:
                heap[0] = last
                heapify_down(0)

            # ---------------------------------
            # Generate next candidate in same row
            # ---------------------------------
            if j + 1 < len(nums2):

                new_pair = [
                    nums1[i] + nums2[j + 1],
                    i,
                    j + 1
                ]

                heap.append(new_pair)
                heapify_up(len(heap) - 1)

        return ans