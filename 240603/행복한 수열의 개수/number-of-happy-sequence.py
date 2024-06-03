n, m = map(int,input().split())

# n * n, 연속해서 m개 이상 -> 행복한 수열

graph = [list(map(int, input().split())) for _ in range(n)]
cnt = 0

# 행 기준
for y in range(n):
    row_cnt = 1
    prev_num = graph[y][0]
    for x in range(1, n):
        if prev_num == graph[y][x] : # prev랑 현재값이랑 같다면
            row_cnt += 1
        else:
            row_cnt = 1
            prev_num = graph[y][x]
    if row_cnt >= m:
        cnt += 1

# 열 기준 
for x in range(n):
    col_cnt = 1
    prev_num = graph[0][x]
    for y in range(1, n):
        if prev_num == graph[y][x] : # prev랑 현재값이랑 같다면
            col_cnt += 1
        else:
            col_cnt = 1
            prev_num = graph[y][x]
    if col_cnt >= m:
        cnt += 1
print(cnt)