class Solution:
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        outdegree = [[] for _ in range(n+1)]
        heap = []
        for element in times:
            u = element[0]
            v = element[1]
            outdegree[u].append((v,element[2]))
        heap.append([0,k])
        dist = [float('inf')] * (n+1)
        dist[k] = 0
        def heapify_up(i):
            while i > 0:

                parent = (i - 1) // 2

                if heap[parent][0] <= heap[i][0]:
                    break

                temp = heap[parent]
                heap[parent] = heap[i]
                heap[i] = temp

                i = parent
        def heapify_down(i):
            while True:
                left = 2*i+1
                right = 2*i+2
                if left>=len(heap):
                    return
                smaller = left
                if right<len(heap) and heap[right]<heap[smaller]:
                    smaller = right
                if heap[smaller]>=heap[i]:
                    return
                temp = heap[i]
                heap[i] = heap[smaller]
                heap[smaller] = temp
                i = smaller
        while len(heap)!=0:
            current= heap[0]
            last  = heap[len(heap)-1]
            heap.pop()
            if len(heap)>0:
                heap[0] = last
                heapify_down(0)
            current_dist = current[0]
            node = current[1]
            if current_dist > dist[node]:
                continue

            for neigh, weight in outdegree[node]:

                new_dist = current_dist + weight

                if new_dist < dist[neigh]:

                    dist[neigh] = new_dist

                    # Insert new candidate
                    heap.append([new_dist, neigh])
                    heapify_up(len(heap) - 1)
        result = 0

        for i in range(1, n + 1):

            if dist[i] == float('inf'):
                return -1

            if dist[i] > result:
                result = dist[i]

        return result