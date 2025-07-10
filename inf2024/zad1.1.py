def alg(n, m, board):
	P = [[False for _ in range(m)] for _ in range(n)]

	P[0][0] = True

	for i in range(n):
		for j in range(m):
			if board[i][j] == 0:
				P[i][j] = False
			else:
				if i == 0 and j != 0:
					P[i][j] = P[i][j - 1]
				elif i != 0 and j == 0:
					P[i][j] = P[i - 1][j]
				elif i != 0 and j != 0:
					P[i][j] = P[i][j - 1] or P[i - 1][j]

	return P[n-1][m-1]

A1 = [
    [1,1,1],
    [0,1,0],
    [1,1,1]
]

A2 = [
    [1,1,1],
    [0,0,1],
    [1,1,1],
    [1,0,0],
    [1,1,1]
]

A3 = [
	[1,0,0,0,0],
	[1,1,0,0,1],
	[0,1,0,0,1],
	[0,1,1,1,0],
	[0,1,0,1,1]
]

print(alg(3,3,A1))
print(alg(5,3,A2))
print(alg(5,5,A3))