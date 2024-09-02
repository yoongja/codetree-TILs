n, m = map(int, input().split())

l = []
for i in range(n):
    row = list(map(int, input().split()))
    l.append(row)

visited = [[False for _ in range(m)] for i in range(n)]

dir = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def dfs(x,y):
    for d in dir:
        nx = x + d[0]
        ny = y + d[1]
        if 0 <= nx < n and 0 <= ny < m and l[nx][ny] == 1 and not visited[nx][ny] :
            visited[nx][ny] = True
            dfs(nx,ny)


visited[0][0] = True
dfs(0,0)
print(visited[n-1][m-1])
if visited[n-1][m-1]:
    print(0)
else:
    print(1)