# Problem: Divide Players Into Teams of Equal Skill - https://leetcode.com/problems/divide-players-into-teams-of-equal-skill/

class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        n = len(skill)
        total = sum(skill)
        target = total * 2 // n
        res = 0
        s = Counter(skill)
        for i in skill:
            if not s[i]:
                continue
            diff = target - i
            if not s[diff]:
                return -1
            res += i*diff
            s[i] -= 1
            s[diff] -= 1
        return res