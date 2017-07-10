import numpy as np
(N,M) = map(int, raw_input().split())
A_ = np.array(map(int, raw_input().split()))
for i in range(M):
	ans = 0
	(x,y) = map(int, raw_input().split())
	A_[x] = y
	A = A_.copy()
	while len(A) != 0:
		if len(A) == max(A):
			A = A[A!=max(A)]
		else:
			ans += 1
			A[np.where(A==min(A))[0][0]] = max(A) - list(A).count(max(A))
			A = A[A!=max(A)]