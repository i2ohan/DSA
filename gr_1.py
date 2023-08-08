N, M = map(int, input().split())

vis = [[False] * M for _ in range(N)]

h = [1, -1, 0, 0]
v = [0, 0, 1, -1]

def dfs(x,y):
    vis[x][y] = True
    for i in range(4):
        dx,dy = x+h[i] , y+v[i]
        if 0 <= dx < N and 0 <= dy < M and not vis[dx][dy]:
            dfs(dx, dy)

cnt = 0

for i in range(N):
    line = input().strip()
    for j in range(M):
        c = line[j]
        vis[i][j] = (c == '#')


for i in range(N):
    for j in range(M):
        if not vis[i][j]:
            dfs(i, j)
            cnt += 1

print(cnt)
