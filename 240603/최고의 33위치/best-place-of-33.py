n = int(input())

graph = [list(map(int,input().split())) for _ in range(n)]

# 3 * 3 크기 격자 내에 들어올 최대 동전의 수
def calculate_coin(s_y, s_x, e_y, e_x):
    earn_coin = 0
    for i in range(s_y, e_y + 1):
        for j in range(s_x, e_x + 1):
            earn_coin += graph[i][j]
    return earn_coin

money = 0
max_money = 0

for y in range(n - 2):
    for x in range(n - 2):
        money = calculate_coin(y, x, y + 2, x + 2)
        max_money = max(money, max_money)

print(max_money)