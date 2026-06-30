class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        left = 0
        current_sum = 0
        min_len = len(nums) + 1

        for right in range(len(nums)):
            current_sum = current_sum + nums[right]

            while current_sum >= target:
                length = right - left + 1

                if length < min_len:
                    min_len = length

                current_sum = current_sum - nums[left]
                left = left + 1

        if min_len == len(nums) + 1:
            return 0

        return min_len