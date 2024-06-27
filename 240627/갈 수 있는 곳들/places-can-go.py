from collections import deque

n, k = map(int, input().split())
# n * n 배열
arr = [list(map(int, input().split())) for _ in range(n)]
# 시작점의 위치를 담는 배열 - 행 열 순서로 담음, 여기서 -1을 해줘야 되는거였음
point = [list(map(int, input().split())) for _  in range(k)]
visited = [[False] * n for _ in range(n)]
ans = 0 # 방문화는 칸의 개수
for i in range(len(point)):
    # point의 개수만큼 수행한다
    q = deque()
    # 출발하는 좌표를 넣어준다
    y = point[i][0] - 1
    x = point[i][1] - 1
    q.append([y,x])

    dx = [0, 0, 1, -1]
    dy = [1,-1, 0, 0]

    while q:
        nowy, nowx = q.popleft() #지금 좌표

        # 0만 갈 수 있음
        for i in range(4):
            nx = nowx + dx[i]
            ny = nowy + dy[i]
            if 0 <= nx < n and 0 <= ny < n and arr[ny][nx] == 0 and not visited[ny][nx]:
                ans += 1
                q.append([ny,nx])
                visited[ny][nx] = True

print(ans)