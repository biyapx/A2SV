# Problem: String Compression - https://leetcode.com/problems/string-compression/

class Solution:
    def compress(self, chars: List[str]) -> int:
        if not chars:
            return 0

        index, i = 0, 0
        while i < len(chars):
            count = 1
            while i + 1 < len(chars) and chars[i] == chars[i+1]:
                i += 1
                count += 1
            chars[index] = chars[i]
            index += 1
            if count > 1:
                for c in str(count):
                    chars[index] = c
                    index += 1
            i += 1
        return index