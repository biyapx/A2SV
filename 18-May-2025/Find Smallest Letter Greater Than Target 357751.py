# Problem: Find Smallest Letter Greater Than Target - https://leetcode.com/problems/find-smallest-letter-greater-than-target/

class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        sorted_norepeat_list = sorted(set(letters))
        
        for letter in sorted_norepeat_list:
            if letter > target:
                return letter
                break
        
        return sorted_norepeat_list[0]
        