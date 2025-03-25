# Problem: Longest Repeating Character Replacement - https://leetcode.com/problems/longest-repeating-character-replacement/

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_count = 0
        max_length = 0
        char_count = {}
        window_start = 0

        for window_end in range(len(s)):
            right_char = s[window_end]
            if right_char not in char_count:
                char_count[right_char] = 0
            char_count[right_char] += 1

            max_count = max(max_count, char_count[right_char])

            if window_end - window_start + 1 - max_count > k:
                left_char = s[window_start]
                char_count[left_char] -= 1
                if char_count[left_char] == 0:
                    del char_count[left_char]
                window_start += 1

            max_length = max(max_length, window_end - window_start + 1)

        return max_length