# Problem: Chat Order - https://codeforces.com/problemset/problem/637/B

n = int(input())
messages = [input().strip() for _ in range(n)]
seen = set()
result = []
for name in reversed(messages):
    if name not in seen:
        seen.add(name)
        result.append(name)
print('\n'.join(result))