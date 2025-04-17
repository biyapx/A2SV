class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        """
        Counts the number of 'good' subarrays where at least k pairs of equal elements exist.
        Uses sliding window technique: expand window to add elements (increasing pairs),
        and shrink from left when condition (k pairs) is met to count valid subarrays.
        
        freq: tracks frequency of each number in current window
        total_pairs: counts all equal-element pairs in window
        """
        n = len(nums)
        left = 0
        count = 0
        total_pairs = 0
        freq = defaultdict(int)

        for right in range(n):
            num = nums[right]
            total_pairs += freq[num]  # Add existing pairs before incrementing
            freq[num] += 1

            # When we have enough pairs, count all subarrays ending at 'right'
            # and try to shrink window from left
            while total_pairs >= k:
                count += n - right  # All remaining elements form valid subarrays
                freq[nums[left]] -= 1
                total_pairs -= freq[nums[left]]  # Remove pairs from the left element
                left += 1

        return count
