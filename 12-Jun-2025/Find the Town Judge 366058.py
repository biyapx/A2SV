# Problem: Find the Town Judge - https://leetcode.com/problems/find-the-town-judge/

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        received = defaultdict(int)
        given = defaultdict(int)

        for a, b in trust:
            given[a] += 1
            received[b] += 1

        for i in range(1, n + 1):
            if given[i] == 0 and received[i] == n - 1:
                return i

        return -1