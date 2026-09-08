class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        sstr = [""]*len(score)
        heap = []
        for i in range(len(score)):
            heap.append([score[i],i])
        def heapify_down(i):
            nonlocal heap
            while True:
                left = 2*i+1
                right = 2*i+2
                if left>=len(heap):
                    break
                larger = left
                if right<len(heap) and heap[larger][0]<heap[right][0]:
                    larger=right
                if heap[larger][0]<heap[i][0]:
                    break
                temp = heap[larger]
                heap[larger] = heap[i]
                heap[i] = temp
                i = larger
        i = len(heap)//2-1
        while i>=0:
            heapify_down(i)
            i-=1
        for i in range(len(heap)):
            root = heap[0]
            heap[0] = heap[len(heap)-1]
            heap.pop()
            sstr[root[1]] = i
            heapify_down(0)
        for i in range(len(score)):
            if sstr[i]==0:
                sstr[i] = "Gold Medal"
            elif sstr[i]==1:
                sstr[i] = "Silver Medal"
            elif sstr[i]==2:
                sstr[i] = "Bronze Medal"
            else:
                sstr[i] = str(sstr[i]+1)
        return sstr