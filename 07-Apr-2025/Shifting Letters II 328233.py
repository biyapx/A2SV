# Problem: Shifting Letters II - https://leetcode.com/problems/shifting-letters-ii/description/

class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        shift_diff = [0] * (n + 1)

        for start, end, direction in shifts:
            if direction == 1:
                shift_diff[start] += 1
                if end + 1 < n:
                    shift_diff[end + 1] -= 1
            else:
                shift_diff[start] -= 1
                if end + 1 < n:
                    shift_diff[end + 1] += 1

        current_shift = 0
        result = []

        for i in range(n):
            current_shift += shift_diff[i]
            normalized_shift = current_shift % 26
            new_char = chr((ord(s[i]) - ord('a') + normalized_shift) % 26 + ord('a')) if normalized_shift != 0 else s[i]
            result.append(new_char)

        return ''.join(result)