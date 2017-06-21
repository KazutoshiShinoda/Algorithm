N = int(raw_input())
row = [0 for i in range(N)]
col = [0 for i in range(N)]
dif1 = [0 for i in range(N)]
dif2 = [0 for i in range(N)]
for i in range(N):
    (row[i], col[i]) = (int(x) for x in raw_input().split())
    dif1[i] = row[i] - col[i]
    dif2[i] = col[i] + row[i]

ans = 0

max_row = max(row)
max_col = max(col)

M = max(max_row, max_col)
for i in range(M+1):
    n = row.count(i)
    m = col.count(i)
    ans += n*(n-1)/2
    ans += m*(m-1)/2
    
min_dif1 = min(dif1)
max_dif1 = max(dif1)

min_dif2 = min(dif2)
max_dif2 = max(dif2)

mini = min(min_dif1, min_dif2)
maxi = max(max_dif1, max_dif2)

for i in range(mini, maxi+1):
    l = dif1.count(i)
    k = dif2.count(i)
    ans += l*(l-1)/2
    ans += k*(k-1)/2

print int(ans)