# Problem: B - The best for Geleta - https://codeforces.com/gym/590201/problem/B

def solve():
    t = int(input())
    for _ in range(t):
        n, m = map(int, input().split())
        a = list(map(int, input().split()))
        operations = []
        for __ in range(m):
            parts = input().split()
            c = parts[0]
            l = int(parts[1])
            r = int(parts[2])
            operations.append((c, l, r))
        
        current_max = max(a)
        res = []
        for c, l, r in operations:
            if l <= current_max <= r:
                if c == '+':
                    current_max += 1
                else:
                    current_max -= 1
            res.append(str(current_max))
        print(' '.join(res))

solve()