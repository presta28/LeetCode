class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        left=0
        right=len(nums)-1
        def merge(nums1:List[int],nums2:List[int]):
            i=0
            j=0
            ans=[]
            while i < len(nums1) and j < len(nums2):
                if nums1[i]<nums2[j]:
                    ans.append(nums1[i])
                    i=i+1
                else:
                    ans.append(nums2[j])
                    j=j+1
            while i < len(nums1):
                ans.append(nums1[i])
                i=i+1
            while j < len(nums2):
                ans.append(nums2[j])
                j=j+1
            return ans
        def divide(left:int,right:int):
            if left == right:
                return [nums[left]]
            mid=(left+right)//2
            arr1=divide(left,mid)
            arr2=divide(mid+1,right)
            arr=merge(arr1,arr2)
            return arr
        return divide(left,right)



        