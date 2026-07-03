class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        ans = set()

        for i in range(len(nums)):
            j = 0
            k = len(nums) - 1

            while j < k:
                if i == j:
                    j += 1
                    continue

                if i == k:
                    k -= 1
                    continue

                pair_sum = nums[j] + nums[k]
                target = -nums[i]

                if target > pair_sum:
                    j += 1

                elif target < pair_sum:
                    k -= 1

                else:
                    triplet = sorted([nums[i], nums[j], nums[k]])
                    ans.add(tuple(triplet))

                    j += 1
                    k -= 1

        return [list(t) for t in ans]
        