# Problem: C - Barking Password - https://codeforces.com/gym/588094/problem/C

target = input().strip()
n = int(input())
words = []
first_char, second_char = target[0], target[1]
can_start = False
can_end = False

for _ in range(n):
    let = input().strip()
    words.append(let)
    if let == target or let == target[::-1]:
        print("YES")
        exit()
    if let[1] == first_char:
        can_start = True
    if let[0] == second_char:
        can_end = True

if can_start and can_end:
    print("YES")
else:
    print("NO")