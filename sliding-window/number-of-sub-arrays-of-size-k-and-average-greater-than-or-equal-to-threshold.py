class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        current_sum = 0
        count=0
        for i in range(k):
            current_sum = current_sum+arr[i]
        if current_sum/k>=threshold:
            count+=1
        for i in range(k,len(arr)):
            current_sum = current_sum+arr[i]-arr[i-k]
            if current_sum/k>=threshold:
                count+=1
        return count
