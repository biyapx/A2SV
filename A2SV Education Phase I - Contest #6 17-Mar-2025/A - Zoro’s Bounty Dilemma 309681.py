# Problem: A - Zoro’s Bounty Dilemma - https://codeforces.com/gym/594356/problem/A

for _ in range(int(input())):
	s = input()
	if '<' in s and '>' in s:
		print('?')
	elif '<' in s:
		print('<')
	elif '>' in s:
		print('>')
	else:
		print('=')