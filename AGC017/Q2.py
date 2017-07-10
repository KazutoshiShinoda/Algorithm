(N, A, B, C, D) = map(int, raw_input().split())
ans = True
if abs(B-A)/float(N) >= D:
	ans = False

if ans:
	print 'YES'
else:
	print 'NO'