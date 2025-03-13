# Problem: B - Card Game - https://codeforces.com/gym/588094/problem/B

def card_game(n):
    cards = list(map(int, input().strip().split()))
    indexed_cards = [(cards[i], i + 1) for i in range(n)]
    indexed_cards.sort()

    pairs = []
    for i in range(n // 2):
        pairs.append((indexed_cards[i][1], indexed_cards[n - 1 - i][1]))

    for pair in pairs:
        print(pair[0], pair[1])

n = int(input())
card_game(n)