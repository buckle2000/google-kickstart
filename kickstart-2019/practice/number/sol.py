def get_ints():
    return map(int, input().split())

T, = get_ints()
for i in range(T):
	A, B = get_ints() # (A, B]
	N, = get_ints()
	while B > A:
		mid = (A+B)//2 + 1
		print(mid)
		feedback = input()
		if feedback == 'TOO_SMALL':
			A = mid
		elif feedback == 'TOO_BIG':
			B = mid - 1
		elif feedback == 'CORRECT':
			break
		elif feedback == 'WRONG_ANSWER':
			raise ValueError(i, A, B, N, mid)
		else:
			raise NotImplementedError('WTF')
