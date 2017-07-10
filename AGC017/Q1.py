(N,P) = map(int, raw_input().split())
A = map(int, raw_input().split())
n_even = 0
m_odd = 0
for i in range(N):
	if A[i] % 2==0:
		n_even += 1
	else:
		m_odd += 1
N = 2**n_even
def calC(a,b):
	l1 = 1
	l2 = 1
	l3 = 1
	for i in range(a):
		l1 *= (i+1)
	for i in range(b):
		l2 *= (i+1)
	for i in range(a-b):
		l3 *= (i+1)
	return l1/l2/l3
M = 0
i = 0	
while i*2+P <= m_odd:
	M += calC(m_odd, i*2+P)
	i += 1

print N*M