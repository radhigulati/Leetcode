def change(n, coins_available):
	# n is target
	coins_so_far = None
	if sum(coins_so_far) == n:
		yield coins_so_far
	elif sum(coins_so_far) > n:
		pass
	elif coins_available == []:
		pass
	else:
		# multiple occurences of the same coin
		for c in change(n, coins_available[:], coins_so_far+[coins_available[0]]):
			yield c
		for c in change(n, coins_available[1:], coins_so_far):
			yield c

n = 5
coins = [1,5,10,25]

solutions = [s for s in change(n, coins, [])]
for s in solutions:
	print(s)