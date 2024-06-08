n= int(input())
graph=[0 for i in range(100)]
lst=[]
for i in range(n):
    a,b=tuple(map(int,input().split()))
    for _ in range(a,b):
        graph[_]+=1
print(max(graph))