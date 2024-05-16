# 특정위치 선택시, 해당 위치를 포함한 양옆 숫자가 반전이 일어남
# 최소 힛수로 선택해서 문자열이 11111이 되도록 하라!

# 두번째 위치가 0이라면 세번째 위치는 꼭 선택되어ㅑ 하고, 만약 두번째가 이미 1이라면 세번째 위치는 절대 선택되어서는 안된다.

n = int(input())
arr = list(map(int,input().split()))

# 만약 1로 만드는 것 불가능 하면 -1출력
cnt = 0 
for i in range(n):
    if i == 0: # 첫번째 일때 영향주는 친구는 두번째 친구
        if arr[i] == 0 and n > 1:
            arr[i] = 1
            arr[i + 1] = abs(arr[i + 1] - 1)
            cnt += 1
        elif arr[i] == 0 and n == 1:
            arr[i] = 1
            cnt += 1
    else:
        if arr[i] == 0 and i + 1 < n:
            arr[i] = 1
            arr[i + 1] = abs(arr[i + 1] - 1)
            cnt += 1
        elif i + 1 == n:
            if arr[i] == 0 and arr[i - 1] == 1:
                cnt = -1
            elif arr[i] == 0 and arr[i - 1] == 0:
                cnt += 1

print(cnt)