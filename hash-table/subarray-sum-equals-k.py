class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        dicts={}
        dicts[k]=[]
        for i in range(1,len(nums)):
            sum=nums[i-1]
            lists=[]
            if sum==k:
                lists.append(sum)
            else:
                lists.append(nums[i-1])
                if sum + nums[i]>k:
                    sum = sum-nums[i-1]
                    lists.remove(nums[i-1])
                sum= sum+nums[i]
                if sum==k:
                    lists.append(nums[i])
                dicts[k].append(lists)
        return len(dicts[k])
        