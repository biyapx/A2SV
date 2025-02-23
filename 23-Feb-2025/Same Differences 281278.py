# Problem: Same Differences - https://codeforces.com/problemset/problem/1520/D

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    
    count = {}
    pairs = 0
    
    for i in range(n):
        diff = a[i] - (i + 1)
        pairs += count.get(diff, 0)
        count[diff] = count.get(diff, 0) + 1
            
    return pairs

t = int(input())
for _ in range(t):
    print(solve())