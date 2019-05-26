for i in range(10):
	for j in range(10):
		if i in [v for v in range(1, 9)]:
			if j in [u for u in range(1, 9)]:
				print(' ', end='')
			else:
				if j == 0:
					print('')
				print('#', end='')
		if i == 0 or i == 9:
			if j == 0 and i != 0:
				print('')
			print('#', end='')