class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        max_heap = []
        for i in range(k):
            max_heap.append(points[i])
        def heapify_down(i,heap_size):
            while True:
                self_distance = (max_heap[i][0])*(max_heap[i][0])+(max_heap[i][1])*(max_heap[i][1])
                left = 2*i+1
                right = 2*i+2
                if left>=heap_size:
                    break
                left_distance = (max_heap[left][0])*(max_heap[left][0])+(max_heap[left][1])*(max_heap[left][1])
                
                larger = left
                if right<heap_size:
                    right_distance = (max_heap[right][0])*(max_heap[right][0])+(max_heap[right][1])*(max_heap[right][1])
                    if right_distance>left_distance:
                        larger = right
                larger_distance = (max_heap[larger][0])*(max_heap[larger][0])+(max_heap[larger][1])*(max_heap[larger][1])
                if larger_distance<self_distance:
                    break
                temp = max_heap[i]
                max_heap[i]=max_heap[larger]
                max_heap[larger]=temp
                i =larger
        i = (k//2)-1
        while i >=0:
            heapify_down(i,k)
            i-=1
        for i in range(k,len(points)):
            self_length = points[i][0] * points[i][0] + points[i][1] * points[i][1]
            if self_length<(max_heap[0][0])*(max_heap[0][0])+(max_heap[0][1])*(max_heap[0][1]):
                max_heap[0] = points[i]
                heapify_down(0,k)
        return max_heap