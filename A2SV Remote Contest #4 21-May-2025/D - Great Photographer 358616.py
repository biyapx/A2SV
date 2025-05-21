# Problem: D - Great Photographer - https://codeforces.com/gym/590201/problem/D

import math

n, x0 = map(int, input().split())

max_a = -math.inf 
min_b = math.inf 

for _ in range(n):
    a, b = map(int, input().split())
    start = min(a, b)
    end = max(a, b)
    max_a = max(max_a, start)
    min_b = min(min_b, end)

if max_a <= min_b:
    if max_a <= x0 <= min_b:
        print(0)
    else:
        
        if x0 < max_a:
            print(max_a - x0)
        else:
            print(x0 - min_b)
else:
    print(-1)