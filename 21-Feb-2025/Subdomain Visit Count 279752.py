# Problem: Subdomain Visit Count - https://leetcode.com/problems/subdomain-visit-count

class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        count = defaultdict(int)

        for s in cpdomains:
            visited, domain = s.split()
            visited = int(visited)
            parts = domain.split('.')
            for i in range(len(parts)):
                subdomain = '.'.join(parts[i:])
                count[subdomain] += visited

        result = [f"{v} {d}" for d, v in count.items()]
        return result