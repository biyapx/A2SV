# Problem: Count Vowel Substrings of a String - https://leetcode.com/problems/count-vowel-substrings-of-a-string/description/

class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        vowel_set = {'a', 'e', 'i', 'o', 'u'}
        count = 0
        n = len(word)

        for start in range(n):
            seen = set()
            for end in range(start, n):
                if word[end] in vowel_set:
                    seen.add(word[end])
                    if len(seen) == 5:
                        count += 1
                else:
                    break

        return count