# Problem: Smallest Value of the Rearranged Number - https://leetcode.com/problems/smallest-value-of-the-rearranged-number/description/

class Solution:
    def smallestNumber(self, num: int) -> int:
        if num < 0:
            digits = sorted(str(num)[1:], reverse=True)
            result = '-' + ''.join(digits)
        else:
            digits = sorted(str(num))
            if digits[0] == '0':
                for i in range(1, len(digits)):
                    if digits[i] != '0':
                        digits[0], digits[i] = digits[i], digits[0]
                        break
            result = ''.join(digits)
        
        return int(result)