# Problem: D - Mugisho and Rufeyda - https://codeforces.com/gym/586622/problem/D

def find_number(n, t):
    if t == 10:
        if n == 1:
            return -1
        else:
            return '1' + '0' * (n - 1)
    
    start_number = 10 ** (n - 1)
    
    if start_number % t == 0:
        return start_number
    else:
        start_number += (t - (start_number % t))
        if start_number < 10 ** n:
            return start_number
        else:
            return -1

n, t = map(int, input().strip().split())
print(find_number(n, t))