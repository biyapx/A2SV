# Problem: C - Robin’s Water Wisdom: Stop the Leaks! - https://codeforces.com/gym/594356/problem/C

def min_holes_to_block(n, A, B, sizes):
    s1 = sizes[0]
    max_size = (s1 * A) / B
    total_size = sum(sizes)
    
    if total_size <= max_size:
        return 0
    
    other_sizes = sizes[1:]
    other_sizes.sort(reverse=True)
    
    blocked_count = 0
    for size in other_sizes:
        total_size -= size
        blocked_count += 1
        if total_size <= max_size:
            return blocked_count
    
    return blocked_count

n, A, B = map(int, input().split())
sizes = list(map(int, input().split()))

print(min_holes_to_block(n, A, B, sizes))