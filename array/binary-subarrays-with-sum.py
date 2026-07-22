class Solution:
    def numSubarraysWithSum(self, nums: List[int], k: int) -> int:
        count=0
        prefix_sum=0
        group={0:1}
        prefix_sum=[nums[0]]
        summ=nums[0]
        for i in range(1,len(nums)):
            summ+=nums[i]
            prefix_sum.append(summ)

        for num in prefix_sum:
            needed_sum = num-k
            if needed_sum in group:
                count+=group[needed_sum]
            if num not in group:
                group[num]=1
            else:
                group[num]+=1
        return count

