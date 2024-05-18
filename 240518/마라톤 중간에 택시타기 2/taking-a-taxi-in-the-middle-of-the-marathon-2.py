n = int(input())

graph = []
for i in range(n):
    a, b = map(int, input().split())
    graph.append([a,b])

min_dis = 1e15 #최단거리

for i in range(1, n-1):
    #현재 건너뛰는 체크포인트 첫번째꺼 마지막꺼 제외!
    #print(graph[i]) 
    dis = 0 
    for j in range(n-2):
        if i == j: # 건너뛰는 것과 같은 인덱스면? 
            dis += abs(graph[i-1][0] - graph[i+1][0]) + abs(graph[i-1][1] - graph[i+1][1])
            #print(dis)
        else: #같은 인덱스가 아니라면?
            dis += abs(graph[i-1][0] - graph[i][0]) + abs(graph[i-1][1] - graph[i][1])
            #print(dis)
    min_dis = min(min_dis, dis)

print(min_dis)