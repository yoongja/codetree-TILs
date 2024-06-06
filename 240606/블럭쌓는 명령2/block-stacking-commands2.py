n,k=map(int,input().split())
graph = [0 for i in range(n+1)]
for i in range(k):
    a,b=map(int,input().split())
    if a!=b:
        for l in range(a,b+1):
            graph[l]+=1
    else:
        graph[a]+=1

print(max(graph))