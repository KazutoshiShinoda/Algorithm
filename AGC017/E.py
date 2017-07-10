(N, H) = map(int, raw_input().split())
X = []
for i in range(N):
	a = map(int, raw_input().split())
	X.append(a)
ans = 'YES'
while len(X)>1:
	n = len(X)
	for i in range(1,n):
		if X[i][3] == 0:
			for j in range(1,n):
				if j != i:
					if X[i][1] == x[j][2]:
						a = [X[i][0], X[j][1], X[i][2], X[j][3]]
						b = X[i]
						c = X[j]
						X.append(a)
						X.remove(b)
						X.remove(c)
						continue
		if X[i][2] == 0:
			for j in range(1,n):
				if j != i:
					if X[i][0] == X[j][3]:
						a = [X[j][0], X[i][1], X[j][2], X[i][3]]
						b = X[i]
						c = X[j]
						X.append(a)
						X.remove(b)
						X.remove(c)
						continue
		ans = 'NO'
		break

print ans