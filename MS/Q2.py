import math
(N, Q) = (int(x) for x in raw_input().split())
max_n = N

ans = N

for n in range(2, max_n):
    m = int(math.log(n, 2))
    if 2**m < n:
	    T = (m+1)*Q + ( N - (2**(m+1)-n)*Q ) / float(n)
    else:
		T = m*Q + N/float(n)
    T = int(math.ceil(T))
    if T < ans:
        ans = T


print ans