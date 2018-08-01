def losange(n):
	for i in range(n):
		text = "*"*i
		print(text.center(n))
	i = n
	while i != 0:
		text = "*"*i
		print(text.center(n))
		i -= 1
	return
