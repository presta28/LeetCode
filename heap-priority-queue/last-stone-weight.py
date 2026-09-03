class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        def heapify_down(i):
            while True:
                left = 2*i+1
                right = 2*i+2
                if left>=len(stones):
                    break
                larger = left
                if right<len(stones) and stones[right]>stones[left]:
                    larger = right
                if stones[larger]<stones[i]:
                    break
                temp = stones[i]
                stones[i] = stones[larger]
                stones[larger]= temp
                i = larger
        def heapify_up(i):
            while i>0:
                parent = (i-1)//2
                if stones[parent]>stones[i]:
                    break
                temp = stones[parent]
                stones[parent] = stones[i]
                stones[i]=temp
                i = parent
        i = len(stones)//2-1
        while i>=0:
            heapify_down(i)
            i-=1
        # Repeatedly take the two largest stones
        while len(stones) > 1:

            # -------- First largest --------
            first = stones[0]

            stones[0] = stones[len(stones) - 1]
            stones.pop()

            if len(stones) > 0:
                heapify_down(0)

            # -------- Second largest --------
            second = stones[0]

            stones[0] = stones[len(stones) - 1]
            stones.pop()

            if len(stones) > 0:
                heapify_down(0)

            # -------- Collision result --------
            if first > second:
                difference = first - second

                stones.append(difference)
                heapify_up(len(stones) - 1)

        if len(stones) == 1:
            return stones[0]

        return 0
        
