import math
def isConnected(C1, C2):
    [x0, y0, r0] = C1
    [x1, y1, r1] = C2
    d_2 = (x1-x0)**2+(y1-y0)**2
    d = math.sqrt(d_2)
    if d > r0 + r1:
        return False
    if d <= r0 + r1:
        return True

T = int(raw_input())
for i in range(T):
    [W, H, N] = map(int, raw_input().split(" "))
    circles = [[0,0,0] for j in range(N)]
    for j in range(N):
        circles[j] = map(int, raw_input().split(" "))
    clusterID = [j for j in range(N)]
    for j in range(N):
        k = 1
        while j+k <= N-1:
            if clusterID[j] != clusterID[j+k]:
                if isConnected(circles[j], circles[j+k]):
                    clusterID[j+k] = clusterID[j]
            k += 1
    maxID = max(clusterID)
    flg = True
    for j in range(maxID+1):
        if j in clusterID:
            top = 0
            bottom = H
            for k in range(N):
                if clusterID[k] == j:
                    tmp_top = circles[k][1]+circles[k][2]
                    tmp_bottom = circles[k][1]-circles[k][2]
                    if top < tmp_top:
                        top = tmp_top
                    if bottom > tmp_bottom:
                        bottom = tmp_bottom
            if top>=H and bottom <= 0:
                flg = False
                break
    if flg:
        print "YES"
    else:
        print "NO"