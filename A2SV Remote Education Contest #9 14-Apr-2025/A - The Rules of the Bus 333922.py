# Problem: A - The Rules of the Bus - https://codeforces.com/gym/603156/problem/A

def check(test_cases):
    results = []
    
    for _ in range(test_cases):
        n = int(input().strip())
        a = list(map(int, input().strip().split()))
        
        seen = set()
        seen.add(a[0])
        
        valid = True
        
        for i in range(1, n):
            current_seat = a[i]
            if current_seat - 1 in seen or current_seat + 1 in seen:
                seen.add(current_seat)
            else:
                valid = False
                break
                
        results.append("YES" if valid else "NO")
    
    print("\n".join(results))

t = int(input())
check(t)