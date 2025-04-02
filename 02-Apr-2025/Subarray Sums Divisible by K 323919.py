# Problem: Subarray Sums Divisible by K - https://leetcode.com/problems/subarray-sums-divisible-by-k/

class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        count = 0
        prefix_sum = 0
        remainder_count = defaultdict(int)
        
        remainder_count[0] = 1
        
        for num in nums:
            prefix_sum += num
            remainder = prefix_sum % k
            
            if remainder < 0:
                remainder += k
            
            count += remainder_count[remainder]
            
            remainder_count[remainder] += 1
            
        return count