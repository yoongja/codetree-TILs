n, t = map(int, input().split())
up_arr = list(map(int, input().split()))
down_arr = list(map(int, input().split()))
down_arr.reverse()

for i in range(t): # t초후
    # 1턴을 도는 것이 1초임
    up_temp = up_arr[-1]
    for j in range(n - 1, 0, -1):
        up_arr[j] = up_arr[j - 1]
    up_arr[0] = down_arr[0]
    for j in range(0, n - 1):
        down_arr[j] = down_arr[j + 1]
    down_arr[-1] = up_temp
down_arr.reverse()
print(*up_arr)
print(*down_arr)