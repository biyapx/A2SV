# Problem: Pow (x, n) - https://leetcode.com/problems/powx-n/

class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0:
            return 1

        if n < 0:
            x = 1 / x
            n = -n

        if n % 2 == 0:
            temp = self.myPow(x, n // 2)
            return temp * temp
        else:
            temp = self.myPow(x, (n - 1) // 2)
            return temp * temp * x