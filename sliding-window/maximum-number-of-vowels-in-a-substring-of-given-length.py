class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = "aeiou"

        current_count = 0

        # first window count
        for i in range(k):
            if s[i] in vowels:
                current_count += 1

        max_count = current_count

        # slide the window
        for i in range(k, len(s)):
            # outgoing character
            if s[i - k] in vowels:
                current_count -= 1

            # incoming character
            if s[i] in vowels:
                current_count += 1

            if current_count > max_count:
                max_count = current_count

        return max_count