# Problem: Less or Equal - https://codeforces.com/problemset/problem/977/C

def lessOrEqual(n, k):
    nums = list(map(int, input().strip().split()))
    nums.sort()
    
    if k == 0:
        return -1 if nums[0] <= 1 else 1
    elif k >= n:
        return nums[-1]
    else:
        if nums[k - 1] == nums[k]:
            return -1
        else:
            return nums[k - 1]

n, k = map(int, input().strip().split())
result = lessOrEqual(n, k)
if result < 1 or result > 10**9:
    print(-1)
else:
    print(result)