class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dicts={}
        for i in range(len(nums)):
            if nums[i] not in dicts:
                dicts[nums[i]]=[]
            dicts[nums[i]].append(i)  
        for num in nums:
            if len(dicts[num])>=2:
                    if dicts[num][-1] - dicts[num][-2]<=k:
                        return True
                    else:
                        dicts[num].pop()
        return False

        