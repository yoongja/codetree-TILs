import sys
sys.setrecursionlimit(10**6)

n = int(input())
graph = []
for i in range(n):
    arr = list(map(int, input().split()))
    graph.append(arr)

visited = [[False] * n for i in range(n)]

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def dfs(x, y, num):
    global bomb
    global count
    
    if count >= 4:
        bomb.add(num)

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and graph[nx][ny] == num:
            visited[nx][ny] = True
            count += 1
            dfs(nx, ny, num)

bomb = set()
count_list = []
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            count = 1
            visited[i][j] = True
            dfs(i, j, graph[i][j])
            count_list.append(count)
count_list.sort()



print(len(bomb), count_list[-1])