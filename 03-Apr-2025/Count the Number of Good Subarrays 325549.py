# Problem: Count the Number of Good Subarrays - https://leetcode.com/problems/count-the-number-of-good-subarrays/description/

class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        n = len(nums)
        left = 0
        count = 0
        total_pairs = 0
        freq = defaultdict(int)
        
        for right in range(n):
            freq[nums[right]] += 1
            total_pairs += freq[nums[right]] - 1
            
            while total_pairs >= k:
                count += n - right
                freq[nums[left]] -= 1
                total_pairs -= freq[nums[left]]
                left += 1
        
        return count