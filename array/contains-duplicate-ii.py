class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dict={}
        lists = []
        for i in range(len(nums)):
            if nums[i] not in dict:
                dict[nums[i]]=[]
            dict[nums[i]].append(i)  
        for num in dict:
            if dict[num][-1] - dict[num][-2]<=k:
                return True
        return False

        