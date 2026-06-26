class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        current_sum=nums[0]
        max_sum=nums[0]
        for i in range(1,len(nums)):
            if nums[i]>nums[i]+current_sum:
                current_sum=nums[i]
            else:
                current_sum=nums[i]+current_sum
            if current_sum>max_sum:
                max_sum=current_sum
        min_sum = nums[len(nums)-1]
        current_sum2=nums[len(nums)-1]
        for i in range(len(nums)-2,-1,-1):
            if nums[i]<current_sum2+nums[i]:
                current_sum2=nums[i]
            else:
                current_sum2 = nums[i]+current_sum2
            if current_sum2 < min_sum:
                min_sum=current_sum2
        result=max(abs(max_sum),abs(min_sum))
        return result
            

        