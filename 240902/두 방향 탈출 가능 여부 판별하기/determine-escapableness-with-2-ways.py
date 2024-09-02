n, m = map(int, input().split())

l = []
for i in range(n):
    row = list(map(int, input().split()))
    l.append(row)

visited = [[0 for _ in range(m)] for _ in range(n)]

dir = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def dfs(x, y):
    for d in dir:
        nx = x + d[0]
        ny = y + d[1]
        if 0 <= nx < n and 0 <= ny < m:
            if l[nx][ny] == 1 and not visited[nx][ny]:
                visited[nx][ny] = 1
                dfs(nx, ny)

# 시작점이 1인 경우에만 탐색을 시작합니다.
if l[0][0] == 1:
    visited[0][0] = 1
    dfs(0, 0)

# 끝점(n-1, m-1)에 도달할 수 있는지 확인
if visited[n - 1][m - 1] == 1:
    print(0)
else:
    print(1)