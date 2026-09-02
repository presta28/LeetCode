class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        nums = []
        n = len(matrix)
        for i in range(n):
            for j in range(n):
                nums.append(matrix[i][j])
        max_heap = []
        for i in range(k):
                max_heap.append(nums[i])
        last_non_leaf = (k//2)-1
        def heapify_down(i,heap_size):
            while True:
                left = 2*i+1
                right = 2*i+2
                if left>=heap_size:
                    break
                larger = left
                if right<heap_size:
                    if max_heap[right]>max_heap[left]:
                        larger = right
                if max_heap[larger]<max_heap[i]:
                    break
                temp = max_heap[i]
                max_heap[i]=max_heap[larger]
                max_heap[larger]=temp
                i = larger
        i = last_non_leaf
        while i >= 0:
            heapify_down(i,k)
            i -= 1
        for i in range(k,len(nums)):
            if max_heap[0]>nums[i]:
                max_heap[0] = nums[i]
                heapify_down(0,k)

        return max_heap[0]
        