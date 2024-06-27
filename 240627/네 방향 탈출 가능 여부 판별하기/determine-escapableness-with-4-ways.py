from collections import deque

n, m = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(m)]

# for i in range(m):
#     arr.append(list(map(int, input().split())))


q = deque()
# 출발하는 좌표를 넣어준다
q.append([0,0])

dx = [0, 0, 1, -1]
dy = [1,-1, 0, 0]

visited = [[False] * n for _ in range(m)]

flag = 0

while q:
    now = q.popleft() #지금 좌표
    x = now[1]
    y = now[0]
    # 1이면 탈출하고 0이면 갈수 없음
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and arr[ny][nx] == 1 and not visited[ny][nx]:
            if nx == n-1 and ny == m-1:
                flag = 1
            q.append([ny,nx])
            visited[ny][nx] = True

print(flag)