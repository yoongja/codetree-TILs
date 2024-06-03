n = int(input())

graph = [list(map(int,input().split())) for _ in range(n)]

# 3 * 3 크기 격자 내에 들어올 최대 동전의 수
def calculate_coin(t):
    earn_coin = 0
    for i in range(3):
        for j in range(3):
            earn_coin += graph[i][t + j]
    return earn_coin


money = 0
max_money = 0

for i in range(n - 2):
    money = calculate_coin(i)
    max_money = max(money, max_money)

print(max_money)