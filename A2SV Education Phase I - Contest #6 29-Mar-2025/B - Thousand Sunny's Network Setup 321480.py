# Problem: B - Thousand Sunny's Network Setup - https://codeforces.com/gym/594356/problem/B

def max_speed(n, k, speeds):
    speeds.sort(reverse=True)
    
    return speeds[k - 1]

n, k = map(int, input().split())
speeds = list(map(int, input().split()))

result = max_speed(n, k, speeds)
print(result)