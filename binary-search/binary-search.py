class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left=0
        right=len(nums)-1
        def binary(nums:List[int],left:int,right:int,target:int):
            if left>right:
                return -1
            mid = (left+right)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]<=target:
                ans=binary(nums,mid+1,right,target)
            else:
                ans=binary(nums,left,mid-1,target)
            return ans
        ans=binary(nums,left,right,target)
        return ans