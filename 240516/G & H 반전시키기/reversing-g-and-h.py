n = int(input())
arr = list(input())
goal_n = list(input())

continue_cnt = 0
cnt = 0
for idx, g in enumerate(goal_n):
    if g == arr[idx]:
        if continue_cnt != 0:
            cnt += 1
        continue_cnt = 0
    else:
        continue_cnt += 1

print(cnt)