class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        i=0
        j=1
        while j<len(nums):
            if nums[j]!=0:
                nums[i],nums[j]=nums[j],nums[i]
                j+=1
                i+=1
            else:
                j+=1
        