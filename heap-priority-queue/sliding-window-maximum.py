class Solution:
    def maxSlidingWindow(
        self,
        nums: List[int],
        k: int
    ) -> List[int]:

        n = len(nums)

        # Is queue mein values nahi, indices store honge
        index_queue = [0] * n

        front = 0
        rear = -1

        # Total windows = n - k + 1
        answer = [0] * (n - k + 1)
        answer_position = 0

        for i in range(n):

            # Step 1:
            # Window se bahar chale gaye indices remove karo
            while (
                front <= rear
                and index_queue[front] <= i - k
            ):
                front = front + 1

            # Step 2:
            # Current element se chhote ya equal elements
            # rear side se remove karo
            while (
                front <= rear
                and nums[index_queue[rear]] <= nums[i]
            ):
                rear = rear - 1

            # Step 3:
            # Current element ka index add karo
            rear = rear + 1
            index_queue[rear] = i

            # Step 4:
            # Complete window banne ke baad maximum save karo
            if i >= k - 1:
                answer[answer_position] = nums[index_queue[front]]
                answer_position = answer_position + 1

        return answer