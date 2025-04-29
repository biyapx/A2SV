# Problem: First Unique Character in a String - https://leetcode.com/problems/first-unique-character-in-a-string/description/?envType=problem-list-v2&envId=queue

class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = Counter(s)
        for i, v in enumerate(s):
            if count[v] == 1:
                return i
                break
        return -1
        