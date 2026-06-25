class Solution:
    def maxSubArray(self, arr: List[int]) -> int:
        max_sum = arr[0]

        for i in range(len(arr)):
            current_sum = arr[i]

            if current_sum > max_sum:
                max_sum = current_sum

            for j in range(i + 1, len(arr)):
                current_sum = current_sum + arr[j]

                if current_sum > max_sum:
                    max_sum = current_sum

        return max_sum