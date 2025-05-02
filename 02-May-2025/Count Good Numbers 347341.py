# Problem: Count Good Numbers - https://leetcode.com/problems/count-good-numbers/

class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD = 10**9 + 7

        def power(base, m):
            result = 1
            #base %= MOD
            #if m == 0:
            #    return 1
            base %= MOD
            #half = power(base, m//2)
            #if m % 2:
            #    return (half * half * base) % MOD
            #return (half * half) % MOD
            
            while m > 0:
                if m%2 == 1:
                    result = (result*base) % MOD
                base = (base*base) % MOD
                m //= 2
            return result
                
        even = (n + 1) // 2
        odd = n // 2

        return (power(5, even) * power(4, odd)) % MOD