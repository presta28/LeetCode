class MedianFinder:

    def __init__(self):
        self.nums = []
        self.heap1 = []
        self.heap2 = []

    def heapify_up_max(self,i:int)->None:
        while i>0:
            parent = (i-1)//2
            if self.heap1[parent]<self.heap1[i]:
                break
            temp = self.heap1[parent]
            self.heap1[parent] = self.heap1[i]
            self.heap1[i] = temp
            i = parent
    def heapify_up_min(self,i:int)->None:
        while i>0:
            parent = (i-1)//2
            if self.heap2[parent]>self.heap2[i]:
                break
            temp = self.heap2[parent]
            self.heap2[parent] = self.heap2[i]
            self.heap2[i] = temp
            i = parent

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
    def findMedian(self) -> float:
        if len(self.nums)==1:
            return self.nums[0]
        return (self.heap1[0]+self.heap2[0])/2
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()