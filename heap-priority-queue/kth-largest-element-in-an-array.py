class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        n = len(nums)

        # -------------------------
        # Heapify Down for Max Heap
        # -------------------------
        def heapify_down(i, heap_size):

            while True:

                left = 2 * i + 1
                right = 2 * i + 2

                # No child
                if left >= heap_size:
                    break

                # Assume left child is larger
                larger = left

                # If right child exists and is larger
                if right < heap_size:
                    if nums[right] > nums[left]:
                        larger = right

                # Current node already >= larger child
                if nums[i] >= nums[larger]:
                    break

                # Manual swap
                temp = nums[i]
                nums[i] = nums[larger]
                nums[larger] = temp

                # Continue from new position
                i = larger

        # -------------------------
        # Build Max Heap
        # -------------------------
        i = (n // 2) - 1

        while i >= 0:
            heapify_down(i, n)
            i -= 1

        # -------------------------
        # Remove largest k-1 times
        # -------------------------
        heap_size = n

        while k > 1:

            # Move last active element to root
            heap_size -= 1

            temp = nums[0]
            nums[0] = nums[heap_size]
            nums[heap_size] = temp

            # Restore Max Heap
            heapify_down(0, heap_size)

            k -= 1

        return nums[0]
        