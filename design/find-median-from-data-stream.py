class MedianFinder:

    def __init__(self):
        self.nums = []
        self.heap1 = []
        self.heap2 = []

    def heapify_up_max(self,i:int)->None:
        while i>0:
            parent = (i-1)//2
            if self.heap1[parent]>=self.heap1[i]:
                break
            temp = self.heap1[parent]
            self.heap1[parent] = self.heap1[i]
            self.heap1[i] = temp
            i = parent
    def heapify_up_min(self,i:int)->None:
        while i>0:
            parent = (i-1)//2
            if self.heap2[parent]<=self.heap2[i]:
                break
            temp = self.heap2[parent]
            self.heap2[parent] = self.heap2[i]
            self.heap2[i] = temp
            i = parent
    def heapify_down_max(self, i: int) -> None:
        while True:
            left = 2 * i + 1
            right = 2 * i + 2

            if left >= len(self.heap1):
                break

            larger = left

            if right < len(self.heap1):
                if self.heap1[right] > self.heap1[left]:
                    larger = right

            if self.heap1[i] >= self.heap1[larger]:
                break

            temp = self.heap1[i]
            self.heap1[i] = self.heap1[larger]
            self.heap1[larger] = temp

            i = larger
    def heapify_down_min(self, i: int) -> None:
        while True:
            left = 2 * i + 1
            right = 2 * i + 2

            if left >= len(self.heap2):
                break

            smaller = left

            if right < len(self.heap2):
                if self.heap2[right] < self.heap2[left]:
                    smaller = right

            if self.heap2[i] <= self.heap2[smaller]:
                break

            temp = self.heap2[i]
            self.heap2[i] = self.heap2[smaller]
            self.heap2[smaller] = temp

            i = smaller

    def addNum(self, num: int) -> None:
        self.nums.append(num)
        if len(self.heap1)==0:
            self.heap1.append(num)
            self.heapify_up_max(len(self.heap1)-1)
        elif num<=self.heap1[0]:
            self.heap1.append(num)
            self.heapify_up_max(len(self.heap1)-1)
        else:
            self.heap2.append(num)
            self.heapify_up_min(len(self.heap2)-1)
        if len(self.heap2) > len(self.heap1):

            value = self.heap2[0]

            # Remove root from min heap
            self.heap2[0] = self.heap2[len(self.heap2) - 1]
            self.heap2.pop()

            if len(self.heap2) > 0:
                self.heapify_down_min(0)

            # Put root into max heap
            self.heap1.append(value)
            self.heapify_up_max(len(self.heap1) - 1)

        # Balance: heap1 can have at most one extra
        elif len(self.heap1) > len(self.heap2) + 1:

            value = self.heap1[0]

            # Remove root from max heap
            self.heap1[0] = self.heap1[len(self.heap1) - 1]
            self.heap1.pop()

            if len(self.heap1) > 0:
                self.heapify_down_max(0)

            # Put root into min heap
            self.heap2.append(value)
            self.heapify_up_min(len(self.heap2) - 1)
    def findMedian(self) -> float:
        if len(self.nums)==1:
            return self.nums[0]
        elif len(self.nums)%2==0:
            return (self.heap1[0]+self.heap2[0])/2
        else:
            return self.heap1[0]




# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()