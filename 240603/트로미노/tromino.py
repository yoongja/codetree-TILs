n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

direction = [
            [[0, 0], [0, 1], [1, 0]],
            [[0, 0], [0, 1], [1, 1]],
            [[0, 0], [1, 0], [1, 1]],
            [[1, 0], [0, 1], [1, 1]],
            [[0, 0], [0, 1], [0, 2]],
            [[0, 0], [1, 0], [2, 0]]
            ]

def calculate(y, x):
    max_cnt = 0
    for dir_1 in direction:
        cnt = 0
        for dy, dx in dir_1:
            ny, nx = y + dy, x + dx
            if 0 <= ny < n and 0 <= nx < m : # 범위안에 들어가면
                cnt += graph[ny][nx]
        max_cnt = max(cnt, max_cnt) 
    return max_cnt


max_cnt = 0
for y in range(n):
    for x in range(m):
        max_cnt = max(max_cnt, calculate(y, x))

print(max_cnt)