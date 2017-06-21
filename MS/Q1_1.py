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

set_row = set(row)
set_col = set(col)
set_dif1 = set(dif1)
set_dif2 = set(dif2)

for i in set_row:
    n = row.count(i)
    ans += n*(n-1)/2

for i in set_col:
    m = col.count(i)
    ans += m*(m-1)/2

for i in set_dif1:
    l = dif1.count(i)
    ans += l*(l-1)/2
    
for i in set_dif2:
    k = dif2.count(i)
    ans += k*(k-1)/2

print int(ans)