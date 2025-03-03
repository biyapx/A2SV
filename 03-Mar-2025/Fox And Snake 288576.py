# Problem: Fox And Snake - https://codeforces.com/problemset/problem/510/A

n, m = map(int, input().strip().split())
result = []

for i in range(n):
    if i % 2 == 0:
        result.append('#' * m)
    else:
        if i % 4 == 1:
            result.append('.' * (m - 1) + '#')
        else:
            result.append('#' + '.' * (m - 1))

for line in result:
    print(line)