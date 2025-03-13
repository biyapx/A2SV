# Problem: A - Nathan is rich - https://codeforces.com/gym/588094/problem/A

t = int(input())
results = []

for _ in range(t):
    n = int(input())
    cars = n // 4
    remaining_wheels = n % 4
    vehicles = cars + (1 if remaining_wheels > 0 else 0)
    results.append(vehicles)

for result in results:
    print(result)