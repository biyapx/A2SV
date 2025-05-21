# Problem: A - Harmonic Melody - https://codeforces.com/gym/590201/problem/A

t = int(input())
res = []

for _ in range(t):
    n = int(input())  
    melo = list(map(int, input().split()))  
    valid = True  
    for i in range(1, len(melo)):
        if abs(melo[i] - melo[i - 1]) not in {5, 7}:
            valid = False 
            break 
    
    if valid:
        res.append("YES")
    else:
        res.append("NO")

for result in res:
    print(result)