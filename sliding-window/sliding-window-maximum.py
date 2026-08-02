class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        new_list=[]
        for i in range(len(nums)-(k-1)):
            max_element=nums[i]
            for j in range(i,i+k):
                if max_element<nums[j]:
                    max_element=nums[j]
            new_list.append(max_element)
        return new_list

        